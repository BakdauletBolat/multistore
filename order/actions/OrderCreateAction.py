from django.db import transaction
from order.actions.OrderConfirmAction import OrderConfirmAction
from order.dto.OrderCreateDto import OrderCreateDto
from order.dto.OrderItemCreateDto import OrderItemCreateDto
from order.models.Order import Order
from order.tasks.AddressCreateTask import AddressCreateTask
from order.tasks.OrderCreateTask import OrderCreateTask
from order.tasks.OrderItemCreateTask import OrderItemCreateTask
from order.tasks.OrderUserCreateTask import OrderUserCreateTask
from order.ui.api.transformers.OrderCreateTransformer import OrderCreateTransformer
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from order.ui.api.transformers.OrderTransformer import OrderTransformer
from django.db.utils import IntegrityError
from rest_framework import status


class OrderCreateAction:
    """Экшен для создание заказа"""

    def __init__(self, data) -> None:
        self.data = data

    def run(self) -> Order:

        with transaction.atomic():
            orderData = OrderCreateTransformer(data=self.data)   # type: ignore
            orderData.is_valid(raise_exception=True)

            userData = orderData.validated_data.pop('user', None)  # type: ignore
            billing_address_data = orderData.validated_data.pop('billing_address', None) # type: ignore
            shipping_address_data = orderData.validated_data.pop('shipping_address', None) # type: ignore
            user = OrderUserCreateTask(userData=userData).run()

            billing_address = AddressCreateTask(dto=billing_address_data,user=user).run()
            shipping_address = AddressCreateTask(dto=shipping_address_data,user=user).run()

            order_items = orderData.validated_data.pop('order_items', [])  # type: ignore

            dto = {
                'status_id':1,
                'user_id':user.id,
                'store_id':1,
                'billing_address_id':billing_address , # type: ignore
                'shipping_address_id':shipping_address, # type: ignore
                'payment_method_id': orderData.validated_data.get('payment_method_id',None),# type: ignore
                'delivery_method_id': orderData.validated_data.get('delivery_method_id',None),  # type: ignore
                'comment':  orderData.validated_data.get('comment',None),# type: ignore
            }
           
            order = OrderCreateTask(dto).run()

            for orderItem in order_items:
                OrderItemCreateTask(dto=OrderItemCreateDto(
                    **orderItem,
                    order_id=order.id  # type: ignore
                )).run()

            return order
