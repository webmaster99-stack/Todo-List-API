from rest_framework import permissions


class IsAuthorOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        """Read and write permissions only for the author"""
        return obj.author == request.user