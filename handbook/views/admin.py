from rest_framework.generics import ListAPIView
from multistore.config.pagination import MiddleResultsSetPagination
from handbook.serializers import CategoryWithParentSerializer,CitySerializer
from handbook.models import Category, City
from rest_framework import filters

# class ProductFilter(filters.FilterSet):
#     store = filters.NumberFilter(field_name="stores__id")
#
#     class Meta:
#         model = Product
#         fields = ['store']


class CategoryListView(ListAPIView):
    serializer_class = CategoryWithParentSerializer
    queryset = Category.objects.all()
    pagination_class = MiddleResultsSetPagination
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['name', 'id']
    ordering = ('id', )


class CitiesListByStoreView(ListAPIView):

    serializer_class = CitySerializer

    def get_queryset(self):
        store = self.request.GET.get('store', None)
        queryset = City.objects.all()
        if store:
            queryset = queryset.filter(stores__in=[store])

        return queryset
