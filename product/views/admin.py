from rest_framework.generics import ListAPIView
from multistore.config.pagination import MiddleResultsSetPagination
from handbook.models import WareHouse
from product.serializers import ProductSerializer, ProductListSerializer, ProductUploadImageSerializer, \
    GetProductPageSerializer, ProductPageSerializer
from product.models import ProductImage, Product, ProductPage
from django_filters import rest_framework as filters
from rest_framework.generics import RetrieveAPIView
from rest_framework.views import APIView
from rest_framework.exceptions import NotFound
from rest_framework.response import Response
from django.db import transaction
from django.shortcuts import get_object_or_404
from multistore.request import StockServiceRequest

request_ims = StockServiceRequest()


class ProductFilter(filters.FilterSet):
    store = filters.NumberFilter(field_name="stores__id")

    class Meta:
        model = Product
        fields = ['store']


class ProductUploadImageView(APIView):

    @staticmethod
    def post(request, pk):
        print(request.data)
        serializer = ProductUploadImageSerializer(data=request.FILES)
        serializer.is_valid(raise_exception=True)
        product = get_object_or_404(Product, id=pk)

        with transaction.atomic():
            images = serializer.validated_data['images']
            for photo in images:
                ProductImage.objects.create(
                    product_id=pk,
                    photo=photo
                )

        return Response(ProductSerializer(product, context={
            'request': request
        }).data, status=201)


class ProductListView(ListAPIView):
    serializer_class = ProductListSerializer
    queryset = Product.objects.all()
    pagination_class = MiddleResultsSetPagination
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = ProductFilter


class ProductDetailView(RetrieveAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()


class ProductGetStockView(APIView):

    @staticmethod
    def get(request, product_id, quality_id):
        warehouses = WareHouse.objects.filter(id__in=[70, 69, 68])
        dict_obj = []
        for warehouse in warehouses:
            response = request_ims.get_stocks_for_product(warehouse.id, product_id, quality_id)
            dict_obj.append({
                'warehouse_name': warehouse.name,
                'stocks': response
            })

        return Response(dict_obj, status=200)


class GetProductPageView(APIView):

    @staticmethod
    def post(request):
        serializer = GetProductPageSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        try:
            product_page = ProductPage.objects.get(**serializer.validated_data)
            return Response(ProductPageSerializer(product_page).data, status=200)
        except Exception:
            raise NotFound('Не найдено такой страницы')


class CreateProductPageView(APIView):

    @staticmethod
    def post(request):
        serializer = ProductPageSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        product_page = ProductPage.objects.create(**serializer.validated_data)
        return Response(ProductPageSerializer(product_page).data, status=200)
