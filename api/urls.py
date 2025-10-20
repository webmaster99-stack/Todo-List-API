from django.urls import path, include
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView
)

urlpatterns = [
    path("auth/", include("accounts.urls")),
    path("todos/", include("todos.urls")),
    path("schema/", SpectacularAPIView.as_view(), name="schema"),
    path("schema/swagger-ui/", SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path("schema/redoc/", SpectacularRedocView.as_view(url_name='schema'), name="redoc")
]
