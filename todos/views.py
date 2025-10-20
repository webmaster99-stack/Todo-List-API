from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from .serializers import TodoSerializer
from .models import Todo
from .paginations import TodoListPaginator
from .filters import TodoFilter
from .permissions import IsAuthorOrReadOnly


class TodoListCreateView(generics.ListCreateAPIView):
    serializer_class = TodoSerializer
    permission_classes = [IsAuthenticated, IsAuthorOrReadOnly]
    filter_backends = [DjangoFilterBackend]
    filterset_class = TodoFilter
    pagination_class = TodoListPaginator

    def get_queryset(self):
        """
        This view returns all uncompleted todos for the current
        authenticated user
        """
        user = self.request.user

        if getattr(self, "swagger_fake_view", False):
            return Todo.objects.none()

        return Todo.objects.filter(author=user, is_completed=False)


class TodoDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TodoSerializer
    permission_classes = [IsAuthenticated, IsAuthorOrReadOnly]
    lookup_field = "pk"

    def get_queryset(self):
        """Only fetch the object if it belongs to the current authenticated user"""
        return Todo.objects.filter(author=self.request.user)
