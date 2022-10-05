from rest_framework.generics import ListAPIView
from multistore.config.pagination import StandartResultsSetPagination
from product.ui.admin.transformers.ProductTransformer import ProductTransformer
from product.models.Product import Product

class ProductListController(ListAPIView):

    serializer_class = ProductTransformer
    queryset = Product.objects.all()
    pagination_class = StandartResultsSetPagination