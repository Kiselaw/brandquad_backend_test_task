from django.contrib import admin

from .models import LogRecord


@admin.register(LogRecord)
class LogEntryAdmin(admin.ModelAdmin):
    list_display = (
        "ip_address",
        "date",
        "http_method",
        "uri",
        "response_code",
        "response_size",
    )
    search_fields = ("ip_address", "uri", "date", "http_method", "response_code")
    list_filter = ("http_method", "response_code")
