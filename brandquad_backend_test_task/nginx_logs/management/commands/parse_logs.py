import datetime as dt
import json
import re

import requests
from django.core.exceptions import ValidationError
from django.core.management.base import BaseCommand

from ...models import LogRecord

GD_DOWNLOAD_LINK = "https://drive.google.com/uc?id={file_id}&export=download"


class Command(BaseCommand):
    """
    Downloads log file from a provided url and adds all the data to the database
    """

    help = "Parse and import nginx logs into the database"

    def add_arguments(self, parser):
        parser.add_argument("file_url", type=str, help="URL to the Nginx log file")

    def handle(self, *args, **options):
        valid_counter = 0
        invalid_counter = 0
        file_url = options["file_url"]
        if "drive.google" in file_url:
            file_id = re.search(r"d/(.+)/", file_url).group(1)
            file_url = GD_DOWNLOAD_LINK.format(file_id=file_id)
        self.stdout.write(self.style.SUCCESS(f"Fetching log file from: {file_url}"))

        # The process of adding data to database is constricted the way it isn't consuming excessive memory
        try:
            response = requests.get(file_url, stream=True)
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            self.stderr.write(
                self.style.ERROR(
                    f"Downloading of the log file failed dut to an error: {e}"
                )
            )
            return

        chunk = []
        try:
            for log_record in response.iter_lines():
                log_record = log_record.decode("utf-8")
                log_record = json.loads(log_record)
                request_data = log_record.get("request", "").split(" ")
                request_method, request_uri = request_data[0], request_data[1]
                log_record = LogRecord(
                    ip_address=log_record.get("remote_ip"),
                    date=dt.datetime.strptime(
                        log_record.get("time"), "%d/%b/%Y:%H:%M:%S %z"
                    ),
                    http_method=request_method,
                    uri=request_uri,
                    response_code=int(log_record.get("response", 0)),
                    response_size=int(log_record.get("bytes", 0)),
                )
                # This triggers model validation
                try:
                    log_record.full_clean()
                    chunk.append(log_record)
                except ValidationError as e:
                    invalid_counter += 1
                if len(chunk) >= 1000:
                    valid_counter += 1000
                    LogRecord.objects.bulk_create(chunk)
                    chunk.clear()
        except json.JSONDecodeError as e:
            invalid_counter += 1

        # Adding a chunk of data to database by using one query
        if chunk:
            valid_counter += len(chunk)
            LogRecord.objects.bulk_create(chunk)

        self.stdout.write(
            self.style.SUCCESS(
                f"File with logs is successfully parsed and {valid_counter} log records are added to the database!"
            )
        )
        if invalid_counter:
            self.stdout.write(
                self.style.ERROR(f"Skipped {invalid_counter} invalid records.")
            )
