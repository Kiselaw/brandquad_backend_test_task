from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import LogRecordViewSet

router = DefaultRouter()
router.register(r"logs", LogRecordViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
