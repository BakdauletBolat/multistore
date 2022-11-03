from handbook.models import Category
from rest_framework.generics import ListAPIView
from handbook.serializers import CategorySerializer
from multistore.config.pagination import StandartResultsSetPagination


class GetTreeCategoriesView(ListAPIView):
    queryset = Category.objects.filter(parent_id=None)
    serializer_class = CategorySerializer
    pagination_class = StandartResultsSetPagination
