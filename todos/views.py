# from rest_framework.response import Response
# from rest_framework import status
# from rest_framework.permissions import IsAuthenticated
# from rest_framework.decorators import api_view, permission_classes
# from .models import Todo
# from .serializers import TodoSerializer
# from .paginations import TodoListPaginator

from rest_framework import generics
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .serializers import TodoSerializer
from .models import Todo


# Create your views here.
# @api_view(["GET"])
# @permission_classes([IsAuthenticated])
# def list_todos(request):
#     todos = Todo.objects.filter(author=request.user, is_completed=False)
#     paginator = TodoListPaginator()
#     paginated_todos = paginator.paginate_queryset(todos, request)
#     serializer = TodoSerializer(paginated_todos, many=True)
#     return paginator.get_paginated_response(serializer.data)
#
#
# @api_view(["POST"])
# @permission_classes([IsAuthenticated])
# def create_todo(request):
#     serializer = TodoSerializer(data=request.data)
#
#     if serializer.is_valid():
#         serializer.save(author=request.user)
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
#
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
# @api_view(["GET"])
# @permission_classes([IsAuthenticated])
# def get_single_todo(request, pk):
#     todo = get_object_or_404(Todo, pk=pk)
#     serializer = TodoSerializer(todo)
#     return Response(serializer.data, status=status.HTTP_200_OK)
#
#
# @api_view(["PUT"])
# @permission_classes([IsAuthenticated])
# def update_todo(request, pk):
#     todo = get_object_or_404(Todo, pk=pk)
#     serializer = TodoSerializer(todo, data=request.data)
#
#     if todo.author != request.user:
#         return Response(
#             {"error": "You are not the author of this todo"},
#             status=status.HTTP_403_FORBIDDEN
#         )
#
#     if serializer.is_valid():
#         serializer.save()
#         return Response(status=status.HTTP_204_NO_CONTENT)
#
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
# @api_view(["DELETE"])
# @permission_classes([IsAuthenticated])
# def delete_todo(request, pk):
#     todo = get_object_or_404(Todo, pk=pk)
#
#     if todo.author != request.user:
#         return Response(
#             {"error": "You are not the author of this todo"},
#             status=status.HTTP_403_FORBIDDEN
#         )
#
#     todo.delete()
#     return Response(status=status.HTTP_204_NO_CONTENT)


class TodoListCreateView(generics.ListCreateAPIView):
    serializer_class = TodoSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """
        This view returns all uncompleted todos for the current
        authenticated user
        """
        user = self.request.user
        return Todo.objects.filter(author=user, is_completed=False)



@permission_classes([IsAuthenticated])
class TodoDetailView(APIView):
    """
    This class-based view is responsible for all primary key based operations
    for todos
    """
    def get(self, request, pk):
        """
        This method is responsible for fetching single object based on primary key
        """
        todo = get_object_or_404(Todo, author=request.user, pk=pk)
        serializer = TodoSerializer(todo)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        """
        This method is responsible for updating a record
        corresponding to a primary key

        :param request: The request coming from the client
        :param pk: The object's primary key passed with the request
        :returns: 204 status code on successful update, 404 status code if a record
        with the given primary key doesn't exist, 403 status code if the user is not
        authorized to update the record
        """
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

    def delete(self, request, pk):
        """
        This method is responsible for deleting a record
        corresponding to a primary key

        :param request: The request coming from the client
        :param pk: The object's primary key passed with the request
        :returns: 204 status code on successful delete, 404 status code if a record
        with the given primary key doesn't exist, 403 status code if the user is not
        authorized to update the record
        """
        todo = get_object_or_404(Todo, pk=pk)

        if todo.author != request.user:
            return Response({"error": "You are not the author of this todo"}, status=status.HTTP_403_FORBIDDEN)

        todo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)