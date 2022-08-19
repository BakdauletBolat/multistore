from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.exceptions import ValidationError
from users.models.User import User
from order.dto.OrderCreateDto import OrderCreateDto
from order.dto.OrderItemCreateDto import OrderItemCreateDto
from order.models.Order import Order
from order.tasks.OrderCreateTask import OrderCreateTask
from order.tasks.OrderItemCreateTask import OrderItemCreateTask
from django.db import transaction
from order.ui.api.transformers.OrderCreateTransformer import OrderCreateTransformer
from django.db.utils import IntegrityError

class OrderCreateController(APIView):
    def post(self,request):
            try:
                with transaction.atomic():
                    orderData = OrderCreateTransformer(data=request.data)
                    orderData.is_valid(raise_exception=True)

                    user = orderData.validated_data.pop('user',None)

                    user = User.objects.create(
                        email=user['email'],
                        last_name=user['last_name'],
                        first_name=user['first_name'],
                        phone=user['phone'],
                    )

                    user.set_password('Zz123456')

                    order_items = orderData.validated_data.pop('order_items',None)
                    
                    order = OrderCreateTask(dto=OrderCreateDto(**orderData.validated_data,
                                                                    status_id=1,
                                                                    user_id=user.id,
                                                                  store_id=1)).run()

                    for orderItem in order_items:
                        print(orderItem['product_id'])
                        OrderItemCreateTask(dto=OrderItemCreateDto(
                            **orderItem,
                            order_id=order.id
                        )).run()
                    
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