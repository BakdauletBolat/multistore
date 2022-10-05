from html import entities
from rest_framework.generics import ListAPIView
from handbook.tasks.GetCategory import GetCategory
from handbook.tasks.GetRecurciveCategoryIdsByParent import GetRecurciveCategoryIdsByParent 
from product.models.Product import Product
from product.tasks.GetProductsByCategoryIds import GetProductsByCategoryIds
from product.ui.api.transformers.ProductBaseTransformer import ProductBaseTransformer
from multistore.config.pagination import StandartResultsSetPagination
from django.db.models import Q 

class FilterProductsController(ListAPIView):

    serializer_class = ProductBaseTransformer
    queryset = Product.objects.all()
    pagination_class = StandartResultsSetPagination

    def get_queryset(self):
        filtersets = self.request.GET
        query_set = Product.objects.all()
        for item in filtersets:
            if item == 'page':
                continue
            elif item == 'per_page':
                continue
            q_object = Q(entities__attribute__name=item,entities__values__name__in=filtersets[item].split(','))
            query_set = query_set.filter(q_object)

        ids = query_set.values_list('id',flat=True)

        return Product.objects.filter(id__in=ids)
