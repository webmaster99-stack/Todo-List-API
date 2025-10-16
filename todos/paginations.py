from rest_framework.pagination import PageNumberPagination

class TodoListPaginator(PageNumberPagination):
    page_size = 3