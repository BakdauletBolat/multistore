from django.db import transaction
from order.serializers import OrderCreateSerializer
from order.models import Order, OrderResponse
from order.tasks.api import OrderChangeAfterAcceptedTask, OrderCreateTask, OrderUserCreateTask, AddressCreateTask, \
    OrderItemCreateTask


class OrderConfirmAction:
    """Экшен для подверждение платежа
    Проверяем статус заявки, в зависомости от кода создаем модель OrderResponse
    и обновляем текущую заявку
    Args:
    dto: (OrderDto)

    Returns:
    order: (Order)
    """

    def __init__(self, dto) -> None:
        self.dto = dto

    def run(self) -> Order:
        order_changed = OrderChangeAfterAcceptedTask(invoice_id=self.dto.pop('invoiceId'),
                                                     code=self.dto['code'],
                                                     datetime=self.dto['dateTime'],
                                                     operation_id=self.dto['id']
                                                     ).run()

        OrderResponse.objects.create(
            order_id=order_changed.id,
            code=self.dto['code'],
            amount=self.dto['amount'],
            email=self.dto['email'],
            dateTime=self.dto['dateTime']
        )

        return order_changed


class OrderAcceptAction:
    """Экшен для принятие платежа"""

    def __init__(self, data) -> None:
        self.data = data

    def run(self) -> Order:
        order_accept_data = OrderCreateSerializer(data=self.data)
        order_accept_data.is_valid(raise_exception=True)
        order = OrderConfirmAction(order_accept_data.validated_data).run()
        return order


class OrderCreateAction:
    """Экшен для создание заказа"""

    def __init__(self, data) -> None:
        self.data = data

    def run(self) -> Order:
        with transaction.atomic():
            order_data = OrderCreateSerializer(data=self.data)
            order_data.is_valid(raise_exception=True)

            order_data = order_data.validated_data.pop('user', None)
            billing_address_data = order_data.validated_data.pop('billing_address', None)
            shipping_address_data = order_data.validated_data.pop('shipping_address', None)
            user = OrderUserCreateTask(userData=order_data).run()

            billing_address = AddressCreateTask(dto=billing_address_data, user=user).run()
            shipping_address = AddressCreateTask(dto=shipping_address_data, user=user).run()

            order_items = order_data.validated_data.pop('order_items', [])

            dto = {
                'status_id': 1,
                'user_id': user.id,
                'store_id': 1,
                'billing_address_id': billing_address,
                'shipping_address_id': shipping_address,
                'payment_method_id': order_data.validated_data.get('payment_method_id', None),
                'delivery_method_id': order_data.validated_data.get('delivery_method_id', None),
                'comment': order_data.validated_data.get('comment', None),
            }

            order = OrderCreateTask(dto).run()

            for order_item in order_items:
                order_item['order_id'] = order.id
                OrderItemCreateTask(data=order_item).run()

            return order
