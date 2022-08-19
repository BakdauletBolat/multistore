from handbook.models.Category import Category
from rest_framework.generics import ListAPIView
from handbook.ui.api.transformers.CategoryTransformer import CategoryTransformer
from multistore.config.pagination import StandartResultsSetPagination


class GetTreeCategories(ListAPIView):
    
    queryset = Category.objects.filter(parent_id=None)
    serializer_class = CategoryTransformer
    pagination_class = StandartResultsSetPagination