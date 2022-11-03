from rest_framework import serializers
from handbook.serializers import CitySerializer, CategoryBaseSerializer
from product.models import Product, ProductBase, ProductImage, Price, PriceType, ProductPage
from handbook.models import Quality
from itertools import groupby
from operator import itemgetter
from store.serializers import StoreSerializer


class ProductPageSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductPage
        fields = ('id', 'title', 'description', 'city', 'store', 'lang', 'product')


class GetProductPageSerializer(serializers.Serializer):
    product_id = serializers.IntegerField(required=True)
    city_id = serializers.IntegerField(required=False)
    store_id = serializers.IntegerField(required=True)
    lang_id = serializers.IntegerField(required=True)


class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ('id', 'photo',)


class PriceTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PriceType
        fields = ('id', 'name')


class QualitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Quality
        fields = ('id', 'name')


class ProductPriceSerializer(serializers.ModelSerializer):
    price_type = PriceTypeSerializer()
    quality = QualitySerializer()

    class Meta:
        model = Price
        fields = ('id', 'cost', 'quality', 'price_type')


class ProductUploadImageSerializer(serializers.Serializer):
    images = serializers.ListField(child=serializers.FileField())


class ProductBaseSerializer(serializers.ModelSerializer):
    category = CategoryBaseSerializer()

    class Meta:
        model = ProductBase
        fields = ('id', 'name', 'category', 'full_name')


class ProductListSerializer(serializers.ModelSerializer):
    base = ProductBaseSerializer()

    class Meta:
        model = Product
        fields = ('id', 'base')


class ProductSerializer(serializers.ModelSerializer):
    entities = serializers.SerializerMethodField(method_name='get_entities')
    base = ProductBaseSerializer()
    stores = StoreSerializer(many=True)
    cities = CitySerializer(many=True)
    images = ProductImageSerializer(many=True)
    prices = serializers.SerializerMethodField('get_prices')

    @staticmethod
    def get_prices(obj):
        return ProductPriceSerializer(obj.base.prices, many=True).data

    @staticmethod
    def get_entities(obj):
        items = obj.entities.values("group__name", 'attribute__name', 'values__name', 'group_id',
                                    'attribute_id').order_by('group__name')
        rows = groupby(items, itemgetter('group__name'))
        objects = []

        for c_title, items in rows:
            group_items = []
            for item in list(items):
                group_items.append({
                    'value': item['values__name'],
                    'group_name': item['group__name'],
                    'attribute_name': item['attribute__name'],
                    'group_id': item['group_id'],
                    'attribute_id': item['attribute_id']
                })
            objects.append({
                'group_name': c_title,
                'items': group_items
            })

        return objects

    class Meta:
        model = Product
        fields = ('id', 'base', 'cities', 'stores', 'entities', 'images', 'prices')
