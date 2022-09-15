from rest_framework import serializers

class BusketQuantiyUpdateTransformer(serializers.Serializer):

    busket_item_id = serializers.IntegerField()
    quantity = serializers.IntegerField(required=False)
    