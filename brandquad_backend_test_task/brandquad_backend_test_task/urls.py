from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/", include("api.urls")),
    path("api/v1/schema/", SpectacularAPIView.as_view(), name="schema"),
    path(
        "api/v1/swagger/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger",
    ),
    path(
        "api/v1/redoc/",
        SpectacularRedocView.as_view(url_name="schema"),
        name="redoc",
    ),
]