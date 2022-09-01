
from order.models.Order import Order
from order.models.OrderResponse import OrderResponse

class OrderConfirmAction:


    def __init__(self,dto) -> None:
        self.dto = dto

    def run(self):
        order = Order.objects.get(uuid=self.dto.validated_data.pop('invoiceId'))

        if self.dto.validated_data['code'] == 'ok':
            order.is_paid = True
            order.operation_id = self.dto.validated_data['id']
            order.paid_date = self.orderAcceptData.validated_data['dateTime']
            order.save()
        
        OrderResponse.objects.create(
                        order_id = order.id,
                        code=self.dto.validated_data['code'],
                        amount =self.dto.validated_data['amount'],
                        email = self.dto.validated_data['email'],
                        dateTime = self.dto.validated_data['dateTime']
                    )

        return order