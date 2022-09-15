from django.db import transaction
from order.actions.OrderConfirmAction import OrderConfirmAction
from order.ui.api.transformers.OrderCreateTransformer import OrderCreateTransformer
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from order.ui.api.transformers.OrderTransformer import OrderTransformer
from django.db.utils import IntegrityError
from rest_framework import status

class OrderAcceptAction:
    """Экшен для принятие платежа"""

    def __init__(self,data) -> None:
        self.data = data
    def run(self)->Response:
        
        try:
            with transaction.atomic():
                orderAcceptData = OrderCreateTransformer(data=self.data)    # type: ignore
                orderAcceptData.is_valid(raise_exception=True)
                order = OrderConfirmAction(orderAcceptData.validated_data).run()
                return Response(data=OrderTransformer(order).data,status=status.HTTP_200_OK)
        except ValidationError as e:
            return Response(data=e.get_full_details(),status=e.status_code)
        except IntegrityError as e:        
            return Response(data={
                'errors': str(e)
            },status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        except Exception as e:
            return Response(data=str(e),status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        