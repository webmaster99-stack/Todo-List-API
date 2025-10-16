from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from .models import Todo
from .serializers import TodoSerializer
from .paginations import TodoListPaginator

# Create your views here.
@api_view(["GET"])
@permission_classes([IsAuthenticated])
def list_todos(request):
    todos = Todo.objects.filter(author=request.user, is_completed=False)
    paginator = TodoListPaginator()
    paginated_todos = paginator.paginate_queryset(todos, request)
    serializer = TodoSerializer(paginated_todos, many=True)
    return paginator.get_paginated_response(serializer.data)


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def create_todo(request):
    serializer = TodoSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save(author=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def get_single_todo(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    serializer = TodoSerializer(todo)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(["PUT"])
@permission_classes([IsAuthenticated])
def update_todo(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    serializer = TodoSerializer(todo, data=request.data)

    if todo.author != request.user:
        return Response(
            {"error": "You are not the author of this todo"},
            status=status.HTTP_403_FORBIDDEN
        )

    if serializer.is_valid():
        serializer.save()
        return Response(status=status.HTTP_204_NO_CONTENT)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["DELETE"])
@permission_classes([IsAuthenticated])
def delete_todo(request, pk):
    todo = get_object_or_404(Todo, pk=pk)

    if todo.author != request.user:
        return Response(
            {"error": "You are not the author of this todo"},
            status=status.HTTP_403_FORBIDDEN
        )

    todo.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)