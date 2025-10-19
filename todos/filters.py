import django_filters
from .models import Todo


class TodoFilter(django_filters.FilterSet):
    priority = django_filters.CharFilter("priority", lookup_expr="iexact")

    class Meta:
        model = Todo
        fields = ["priority"]
