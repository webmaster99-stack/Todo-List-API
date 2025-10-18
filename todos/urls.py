from django.urls import path
from . import views

urlpatterns = [
    # path("list_todos", views.list_todos, name="list_todos"),
    # path("create_todo/", views.create_todo, name="create_todo"),
    # path("todo_detail/<int:pk>/", views.get_single_todo, name="todo_detail"),
    # path("update_todo/<int:pk>/", views.update_todo, name="update_todo"),
    # path("delete_todo/<int:pk>/", views.delete_todo, name="delete_todo")
    path("list_create_todo/", views.TodoListCreateView.as_view(), name="list_create_todo"),
    path("todo_detail/<int:pk>/", views.TodoDetailView.as_view(), name="retrieve_update_delete_todo"),
]