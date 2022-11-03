from rest_framework import serializers
from stock.models import Stock
from product.serializers import ProductBaseSerializer
from handbook.serializers import WareHouseSerializer


class StockSerializer(serializers.ModelSerializer):
    product = ProductBaseSerializer
    WareHouse = WareHouseSerializer

    class Meta:
        model = Stock
        fields = ('id', 'quality', 'store', 'WareHouse', 'product', 'quantity')


class StockFilterSerializer(serializers.Serializer):
    city_id = serializers.IntegerField()
    product_id = serializers.IntegerField()
