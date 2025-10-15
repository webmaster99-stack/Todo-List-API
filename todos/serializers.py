from rest_framework import serializers
from.models import Todo
from accounts.models import CustomUser


class SimpleAuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ["id", "username", "first_name", "last_name"]


class TodoSerializer(serializers.ModelSerializer):
    author = SimpleAuthorSerializer(read_only=True)
    class Meta:
        model = Todo
        fields = ["id", "title", "description", "priority", "is_completed", "author"]
