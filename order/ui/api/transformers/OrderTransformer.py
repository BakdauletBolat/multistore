from rest_framework import serializers
from order.ui.api.transformers.OrderCreateTransformer import AddressTransformer
from store.models.Store import Store
from order.models.Order import Order
from order.models.PaymentMethod import PaymentMethod
from order.models.OrderItem import OrderItem
from order.models.DeliveryMethod import DeliveryMethod
from users.ui.api.transformers.UserTransformer import UsersTransformer


class PaymentMethodTransformer(serializers.ModelSerializer):

    class Meta:
        model = PaymentMethod
        fields = ('id','name')


class DeliveryMethodTransformer(serializers.ModelSerializer):

    class Meta:
        model = DeliveryMethod
        fields = ('id','name')



class StoreTransformer(serializers.ModelSerializer):

    class Meta:
        model = Store
        fields = ('id','name')


class OrderItemTransformer(serializers.ModelSerializer):

    class Meta:
        model = OrderItem
        fields = ('id','product','quantity','cost')


class OrderTransformer(serializers.ModelSerializer):

    user = UsersTransformer(read_only=True)
    payment_method = PaymentMethodTransformer(read_only=True)
    delivery_method = DeliveryMethodTransformer(read_only=True)
    store = StoreTransformer(read_only=True)
    shipping_address = AddressTransformer(read_only=True)
    billing_address = AddressTransformer(read_only=True)
    order_items = OrderItemTransformer(read_only=True,many=True)

    class Meta:
        model = Order
        fields = ('id','uuid','user','order_items','created_date','updated_date','status','payment_method','delivery_method','shipping_address','billing_address','store','comment')