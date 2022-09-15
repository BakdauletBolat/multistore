from order.models.Order import Order


class OrderChangeAfterAcceptedAction:
    """Экшен для изменение заказа на оплачен или не оплачен"""
    def __init__(self,code:str,datetime,operation_id:int,invoice_id) -> None:
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
