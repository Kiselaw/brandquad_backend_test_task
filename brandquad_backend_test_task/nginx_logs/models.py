from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

HTTP_METHOD_CHOICES = [
    ("GET", "GET"),
    ("POST", "POST"),
    ("PUT", "PUT"),
    ("DELETE", "DELETE"),
    ("PATCH", "PATCH"),
    ("HEAD", "HEAD"),
    ("OPTIONS", "OPTIONS"),
]


class LogRecord(models.Model):
    ip_address = models.GenericIPAddressField(blank=False, null=False)
    date = models.DateTimeField(blank=False, null=False)
    http_method = models.CharField(
        max_length=7, choices=HTTP_METHOD_CHOICES, blank=False, null=False
    )
    uri = models.CharField(max_length=1000, blank=False, null=False)
    response_code = models.IntegerField(
        validators=[MinValueValidator(100), MaxValueValidator(599)],
        blank=False,
        null=False,
    )
    response_size = models.IntegerField(blank=False, null=False)

    class Meta:
        verbose_name = "Log record"
        verbose_name_plural = "Log records"
