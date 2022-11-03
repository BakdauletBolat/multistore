from rest_framework import serializers
from order.models import Order, OrderItem, DeliveryMethod, PaymentMethod
from users.serializers import UserSerializer
from store.serializers import StoreSerializer


class OrderAcceptSerializer(serializers.Serializer):
    id = serializers.CharField()
    dateTime = serializers.DateTimeField()
    invoiceId = serializers.CharField()
    amount = serializers.IntegerField()
    issuer = serializers.CharField()
    code = serializers.CharField()
    email = serializers.CharField()
    phone = serializers.CharField()


class OrderUserSerializer(serializers.Serializer):
    last_name = serializers.CharField()
    first_name = serializers.CharField()
    email = serializers.EmailField()
    phone = serializers.CharField()


class OrderItemSerializer(serializers.Serializer):
    product_id = serializers.IntegerField()
    quantity = serializers.IntegerField()
    cost = serializers.IntegerField()


class AddressSerializer(serializers.Serializer):
    city_id = serializers.IntegerField()
    street = serializers.CharField(max_length=255)
    number_house = serializers.CharField(max_length=255)
    number_flat = serializers.CharField(max_length=255, required=False)


class OrderCreateSerializer(serializers.Serializer):
    """Трансформер для валидаций данных"""

    user = OrderUserSerializer()
    operation_id = serializers.IntegerField(required=False)
    order_items = OrderItemSerializer(many=True)
    payment_method_id = serializers.IntegerField()
    delivery_method_id = serializers.IntegerField()
    comment = serializers.CharField(required=False)
    shipping_address = AddressSerializer(required=False)
    billing_address = AddressSerializer(required=False)


class PaymentMethodSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentMethod
        fields = ('id', 'name')


class DeliveryMethodSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeliveryMethod
        fields = ('id', 'name')


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ('id', 'product', 'quantity', 'cost')


class OrderSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    payment_method = PaymentMethodSerializer(read_only=True)
    delivery_method = DeliveryMethodSerializer(read_only=True)
    store = StoreSerializer(read_only=True)
    shipping_address = AddressSerializer(read_only=True)
    billing_address = AddressSerializer(read_only=True)
    order_items = OrderItemSerializer(read_only=True, many=True)

    class Meta:
        model = Order
        fields = ('id', 'uuid', 'user', 'order_items', 'created_date', 'updated_date', 'status', 'payment_method',
                  'delivery_method', 'shipping_address', 'billing_address', 'store', 'comment')
