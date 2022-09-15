from rest_framework import serializers

from busket.models.BusketItem import BusketItem

class BusketItemTransformer(serializers.ModelSerializer):

    class Meta:

        fields = ('__all__')
        model = BusketItem


class BusketCreateTransformer(serializers.Serializer):

    product_id = serializers.IntegerField()
    quantity = serializers.IntegerField()
    busket_id = serializers.IntegerField(required=False)
    