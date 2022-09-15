from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.exceptions import ValidationError
from order.actions.OrderCreateAction import OrderCreateAction
from order.ui.api.transformers.OrderTransformer import OrderTransformer
from order.models.Order import Order
from django.db.utils import IntegrityError

class OrderCreateController(APIView):
    """Веб контроллер для создание заказа"""
    
    def post(self,request) -> Response:
            try:
                order:Order = OrderCreateAction(data=request.data).run()
                return Response(data=OrderTransformer(order).data,status=status.HTTP_200_OK)
            except ValidationError as e:
                return Response(data=e.get_full_details(),status=e.status_code)
            
            except IntegrityError as e:        
                return Response(data={
                    'errors': str(e)
                },status=status.HTTP_500_INTERNAL_SERVER_ERROR)

            except Exception as e:
                return Response(data=str(e),status=status.HTTP_500_INTERNAL_SERVER_ERROR)