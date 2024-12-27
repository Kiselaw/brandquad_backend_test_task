from rest_framework import serializers

from nginx_logs.models import LogRecord


class LogRecordSerializer(serializers.ModelSerializer):
    """
    Serializer for all LogRecord fields
    """

    class Meta:
        model = LogRecord
        fields = "__all__"
