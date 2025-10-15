from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.root, name="root"),
    path("health", views.health_check, name="health_check"),
    path("auth/", include("accounts.urls")),
    path("todos/", include("todos.urls")),
]