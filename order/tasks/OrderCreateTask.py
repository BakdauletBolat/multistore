
from order.models.Order import Order

class OrderCreateTask:


    def __init__(self,dto:dict) -> None:
        self.dto = dto

    def run(self)->Order:
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