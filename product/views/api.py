from typing import Any
from django.db.models import Q
from rest_framework.generics import ListAPIView
from handbook.tasks.api import GetCategory, GetRecurciveCategoryIdsByParent
from product.models import Product
from product.tasks.api import GetProductsByCategoryIds
from product.serializers import ProductSerializer
from multistore.config.pagination import StandartResultsSetPagination
from rest_framework.exceptions import ValidationError, NotFound


class ProductsByCategoryIdView(ListAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    pagination_class = StandartResultsSetPagination

    def get_queryset(self, *args, **kwargs):
        category_id: Any | None = self.kwargs.get('category_id', None)

        if category_id is not None:
            main_category = GetCategory(id=category_id, store_id=1).run()

            ids = GetRecurciveCategoryIdsByParent(main_category=main_category, store_id=1).run()
            products = GetProductsByCategoryIds(ids=ids).run()

            return products

        raise ValidationError(detail='category_id not specified')


class FilterProductsView(ListAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    pagination_class = StandartResultsSetPagination

    def get_queryset(self):
        pk = self.kwargs.get('pk', None)
        if pk is None:
            raise NotFound()

        filtersets = self.request.GET
        query_set = Product.objects.all()
        for item in filtersets:
            if item == 'page':
                continue
            elif item == 'per_page':
                continue
            q_object = Q(entities__category_id=pk, entities__attribute__name=item,
                         entities__values__name__in=filtersets[item].split(','))
            query_set = query_set.filter(q_object)

        ids = query_set.values_list('id', flat=True)

        return Product.objects.filter(id__in=ids)
