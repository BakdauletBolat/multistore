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
    

class OrderCreateTransformer(serializers.Serializer):
    
    user = OrderUserTransformer()
    operation_id = serializers.IntegerField(required=False)
    order_items = OrderItemTransformer(many=True)
    payment_method_id = serializers.IntegerField()
    delivery_method_id = serializers.IntegerField()
    comment = serializers.CharField(required=False)
    shipping_address = serializers.CharField(required=False)
    billing_address = serializers.CharField(required=False)
     