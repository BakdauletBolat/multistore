

from order.dto.OrderItemCreateDto import OrderItemCreateDto
from order.models.OrderItem import OrderItem

class OrderItemCreateTask:


    def __init__(self,dto:OrderItemCreateDto) -> None:
        self.dto = dto

    def run(self):
        print(self.dto)
        orderItem = OrderItem.objects.create(
                product_id=self.dto.product_id,
                quantity=self.dto.quantity,
                order_id=self.dto.order_id,
                cost=self.dto.cost
            )

        return orderItem