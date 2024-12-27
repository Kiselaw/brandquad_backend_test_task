from rest_framework.pagination import LimitOffsetPagination


class CustomLimitOffsetPagination(LimitOffsetPagination):
    """
    Custom pagination rules
    """

    default_limit = 100
    max_limit = 500
