from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.exceptions import ValidationError
from order.ui.api.transformers.OrderAcceptTransformer import OrderAcceptTransformer
from users.models.User import User
from order.dto.OrderCreateDto import OrderCreateDto
from order.dto.OrderItemCreateDto import OrderItemCreateDto
from order.models.Order import Order
from order.models.OrderResponse import OrderResponse
from order.tasks.OrderCreateTask import OrderCreateTask
from order.tasks.OrderItemCreateTask import OrderItemCreateTask
from django.db import transaction

from order.ui.api.transformers.OrderCreateTransformer import OrderCreateTransformer
from django.db.utils import IntegrityError

class OrderAcceptController(APIView):
    def post(self,request):
            remote_addr = self.request.META.get('REMOTE_ADDR',None)
            print(remote_addr)
            if remote_addr is not None and remote_addr == '193.93.56.115':
                try:
                    with transaction.atomic():
                        orderAcceptData = OrderAcceptTransformer(data=request.data)
                        orderAcceptData.is_valid(raise_exception=True)

                        order = Order.objects.get(uuid=orderAcceptData.validated_data.pop('invoiceId'))

                        if orderAcceptData.validated_data['code'] == 'ok':
                           order.is_paid = True
                           order.paid_date = orderAcceptData.validated_data['dateTime']
                           order.save()

                        orderResponse = OrderResponse.objects.create(
                            order_id = order.id,
                            code=orderAcceptData.validated_data['code'],
                            amount =orderAcceptData.validated_data['amount'],
                            email = orderAcceptData.validated_data['email'],
                            dateTime = orderAcceptData.validated_data['dateTime']
                        )

                        return Response(data={'status':'ok'},status=status.HTTP_200_OK)
                except ValidationError as e:
                    return Response(data=e.get_full_details(),status=e.status_code)
                
        
                except IntegrityError as e:        
                    return Response(data={
                        'errors': str(e)
                    },status=status.HTTP_500_INTERNAL_SERVER_ERROR)

                except Exception as e:
                    print(type(e))

                    return Response(data=str(e),status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            else:
                return Response(data={'errors':'not acceptable'},status=status.HTTP_406_NOT_ACCEPTABLE)