from django.db import models
from accounts.models import CustomUser

# Create your models here.
class Todo(models.Model):

    priority_choices = [
        ("Low", "Low"),
        ("Medium", "Medium"),
        ("High", "High")
    ]

    title = models.CharField(max_length=50, null=True, blank=True)
    description = models.CharField(max_length=255, null=True, blank=True)
    priority = models.CharField(choices=priority_choices, max_length=50, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_completed = models.BooleanField(default=False)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="todos", null=True, blank=True)

    def __str__(self):
        return self.title