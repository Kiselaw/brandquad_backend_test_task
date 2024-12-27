from datetime import datetime

from django.core.exceptions import ValidationError
from django.test import TestCase
from django.utils.timezone import make_aware

from .models import LogRecord


class LogRecordTestCase(TestCase):
    """
    Test cases for CRUD operations
    """

    def setUp(self):
        # Valid data
        self.valid_data = {
            "ip_address": "192.168.1.1",
            "date": make_aware(datetime(2024, 12, 27, 12, 0)),
            "http_method": "GET",
            "uri": "/api/data",
            "response_code": 200,
            "response_size": 1234,
        }
        self.log_record = LogRecord.objects.create(**self.valid_data)

    def test_create_log_record(self):
        log = LogRecord.objects.create(**self.valid_data)
        self.assertEqual(log.ip_address, "192.168.1.1")
        self.assertEqual(log.http_method, "GET")
        self.assertEqual(log.response_code, 200)
        self.assertEqual(log.response_size, 1234)

    def test_create_log_record_with_invalid_ip(self):
        invalid_data = self.valid_data.copy()
        invalid_data["ip_address"] = "invalid_ip"
        with self.assertRaises(ValidationError):
            log = LogRecord(**invalid_data)
            log.full_clean()

    def test_create_log_record_with_invalid_http_method(self):
        invalid_data = self.valid_data.copy()
        invalid_data["http_method"] = "INVALIDMETHOD"
        with self.assertRaises(ValidationError):
            log = LogRecord(**invalid_data)
            log.full_clean()

    def test_create_log_record_with_invalid_response_code(self):
        invalid_data = self.valid_data.copy()
        invalid_data["response_code"] = 600
        with self.assertRaises(ValidationError):
            log = LogRecord.objects.create(**invalid_data)
            log.full_clean()

    def test_read_log_record(self):
        log = LogRecord.objects.get(id=self.log_record.id)
        self.assertEqual(log.ip_address, "192.168.1.1")
        self.assertEqual(log.http_method, "GET")

    def test_update_log_record(self):
        self.log_record.http_method = "POST"
        self.log_record.response_size = 5678
        self.log_record.save()

        updated_log = LogRecord.objects.get(id=self.log_record.id)
        self.assertEqual(updated_log.http_method, "POST")
        self.assertEqual(updated_log.response_size, 5678)

    def test_update_log_record_with_invalid_response_code(self):
        self.log_record.response_code = 600
        with self.assertRaises(ValidationError):
            self.log_record.full_clean()

    def test_delete_log_record(self):
        log_id = self.log_record.id
        self.log_record.delete()
        with self.assertRaises(LogRecord.DoesNotExist):
            LogRecord.objects.get(id=log_id)

    def test_create_log_record_with_missing_required_fields(self):
        invalid_data = self.valid_data.copy()
        del invalid_data["uri"]
        with self.assertRaises(ValidationError):
            log = LogRecord.objects.create(**invalid_data)
            log.full_clean()

    def test_create_log_record_with_invalid_uri(self):
        invalid_data = self.valid_data.copy()
        invalid_data["uri"] = "a" * 2000
        with self.assertRaises(ValidationError):
            log = LogRecord(**invalid_data)
            log.full_clean()
