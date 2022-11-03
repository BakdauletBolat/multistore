from rest_framework import serializers
from busket.models import BusketItem, Busket


class BusketItemSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = BusketItem


class BusketCreateSerializer(serializers.Serializer):
    product_id = serializers.IntegerField()
    quantity = serializers.IntegerField()
    busket_id = serializers.IntegerField(required=False)


class BusketQuantiyUpdateSerializer(serializers.Serializer):
    busket_item_id = serializers.IntegerField()
    quantity = serializers.IntegerField(required=False)


class BusketSerializer(serializers.ModelSerializer):
    items = BusketItemSerializer(many=True)

    class Meta:
        fields = '__all__'
        model = Busket
