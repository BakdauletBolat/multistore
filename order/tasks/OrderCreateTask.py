

from order.dto.OrderCreateDto import OrderCreateDto
from order.models.Order import Order

class OrderCreateTask:


    def __init__(self,dto:OrderCreateDto) -> None:
        self.dto = dto

    def run(self):
        order = Order.objects.create(
                status_id=self.dto.status_id,
                payment_method_id=self.dto.payment_method_id,
                delivery_method_id=self.dto.delivery_method_id,
                user_id=self.dto.user_id,
                store_id=1,
                billing_address=self.dto.billing_address,
                shipping_address=self.dto.shipping_address,
                comment=self.dto.comment
            )

        return order