from rest_framework.pagination import PageNumberPagination


class StandartResultsSetPagination(PageNumberPagination):
    page_size = 20
    max_page_size = 1000