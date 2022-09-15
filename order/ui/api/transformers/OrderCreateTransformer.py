from rest_framework import serializers


class OrderUserTransformer(serializers.Serializer):

    last_name = serializers.CharField()
    first_name = serializers.CharField()
    email = serializers.EmailField()
    phone = serializers.CharField()

class OrderItemTransformer(serializers.Serializer):

    product_id = serializers.IntegerField()
    quantity = serializers.IntegerField()
    cost = serializers.IntegerField()


class AddressTransformer(serializers.Serializer):
    city_id = serializers.IntegerField()
    street = serializers.CharField(max_length=255)
    number_house = serializers.CharField(max_length=255)
    number_flat = serializers.CharField(max_length=255,required=False)


class OrderCreateTransformer(serializers.Serializer):
    """Трансформер для валидаций данных"""
    
    user = OrderUserTransformer()
    operation_id = serializers.IntegerField(required=False)
    order_items = OrderItemTransformer(many=True)
    payment_method_id = serializers.IntegerField()
    delivery_method_id = serializers.IntegerField()
    comment = serializers.CharField(required=False)
    shipping_address = AddressTransformer(required=False)
    billing_address = AddressTransformer(required=False)
     