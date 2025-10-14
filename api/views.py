from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view


# Create your views here.
@api_view(["GET"])
def root(request):
    return Response({"message": "Welcome to Todo List API"}, status=status.HTTP_200_OK)


@api_view(["GET"])
def health_check(request):
    return Response({"status": "healthy"}, status=status.HTTP_200_OK)