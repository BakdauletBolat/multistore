from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.exceptions import ValidationError
from order.tasks.OrderConfirmAction import OrderConfirmAction
from order.ui.api.transformers.OrderAcceptTransformer import OrderAcceptTransformer

from django.db import transaction

from order.ui.api.transformers.OrderTransformer import OrderTransformer
from django.db.utils import IntegrityError

class OrderAcceptController(APIView):

    def get_client_ip(self,request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[-1].strip()
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip

    def post(self,request):
            remote_addr = self.get_client_ip(request)
            if remote_addr is not None and remote_addr == '10.10.1.1':
                try:
                    with transaction.atomic():
                        orderAcceptData = OrderAcceptTransformer(data=request.data)
                        orderAcceptData.is_valid(raise_exception=True)

                        order = OrderConfirmAction(orderAcceptData)
                        
                        return Response(data={'status':OrderTransformer(order).data},status=status.HTTP_200_OK)
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