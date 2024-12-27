from rest_framework import viewsets

from nginx_logs.models import LogRecord

from .paginators import CustomLimitOffsetPagination
from .serializers import LogRecordSerializer


class LogRecordViewSet(viewsets.ModelViewSet):
    """
    Provides all CRUD operations for the LogRecord model
    """

    queryset = LogRecord.objects.all()
    serializer_class = LogRecordSerializer
    pagination_class = CustomLimitOffsetPagination
