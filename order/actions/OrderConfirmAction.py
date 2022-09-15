
from order.models.Order import Order
from order.models.OrderResponse import OrderResponse
from order.tasks.OrderChangeAfterAcceptedAction import OrderChangeAfterAcceptedAction

class OrderConfirmAction:
    """Экшен для подверждение платежа
    Проверяем статус заявки, в зависомости от кода создаем модель OrderResponse
    и обновляем текущую заявку
    Args:
        dto: (OrderDto)

    Returns:
        order: (Order)
    """

    def __init__(self,dto) -> None:
        self.dto = dto

    def run(self)->Order:
        orderChanged = OrderChangeAfterAcceptedAction(invoice_id=self.dto.pop('invoiceId'),
                                                code=self.dto['code'],
                                                datetime=self.dto['dateTime'],
                                                operation_id=self.dto['id']
                                                ).run()
        
        OrderResponse.objects.create(
                        order_id = orderChanged.id,  # type: ignore
                        code=self.dto['code'],
                        amount =self.dto['amount'],
                        email = self.dto['email'],
                        dateTime = self.dto['dateTime']
                    )

        return orderChanged