from order.models import Order, Address, OrderItem
from users.models import User
from typing import Optional


class OrderCreateTask:

    def __init__(self, dto: dict) -> None:
        self.dto = dto

    def run(self) -> Order:
        order = Order.objects.create(
            status_id=self.dto['status_id'],
            payment_method_id=self.dto['payment_method_id'],
            delivery_method_id=self.dto['delivery_method_id'],
            billing_address_id=self.dto['billing_address_id'],
            shipping_address_id=self.dto['shipping_address_id'],
            user_id=self.dto['user_id'],
            store_id=1,
            comment=self.dto['comment']
        )

        return order


class AddressCreateTask:

    def __init__(self, dto: Optional[dict], user: User) -> None:
        self.dto = dto
        self.user = user

    def run(self) -> Optional[int]:
        if self.dto is not None:
            return Address.objects.create(
                city_id=self.dto['city_id'],
                street=self.dto['street'],
                user=self.user,
                number_house=self.dto['number_house'],
                number_flat=self.dto.get('number_flat', None),

            ).id

        return None


class OrderChangeAfterAcceptedTask:
    """Экшен для изменение заказа на оплачен или не оплачен"""

    def __init__(self, code: str, datetime, operation_id: int, invoice_id) -> None:
        self.code = code
        self.datetime = datetime
        self.invoice_id = invoice_id
        self.operation_id = operation_id

    def run(self) -> Order:
        order = Order.objects.get(uuid=self.invoice_id)

        if self.code == 'ok':
            order.is_paid = True
            order.operation_id = self.operation_id
            order.paid_date = self.datetime
            order.save()
        return order


class OrderUserCreateTask:

    def __init__(self, user_data) -> None:
        self.user_data = user_data

    def run(self):

        try:
            user = User.objects.get(phone=self.user_data['phone'])
        except User.DoesNotExist:
            try:
                user = User.objects.get(email=self.user_data['email'])
            except User.DoesNotExist:
                user = User.objects.create(
                    email=self.user_data['email'],
                    last_name=self.user_data['last_name'],
                    first_name=self.user_data['first_name'],
                    phone=self.user_data['phone'],
                )
                user.set_password('Zz123456')
                user.save()

        return user


class OrderItemCreateTask:

    def __init__(self, data: dict) -> None:
        self.data = data

    def run(self):
        order_item = OrderItem.objects.create(**self.data)
        return order_item
