from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from order.actions.OrderAcceptAction import OrderAcceptAction
from rest_framework.request import Request


class OrderAcceptController(APIView):
    """Веб контроллер для принятие платежей"""

    def get_client_ip(self,request:Request)->str:
        """Сервис для получение ip клиента"""

        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[-1].strip()
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip

    def post(self,request:Request) -> Response:

            remote_addr:str = self.get_client_ip(request)

            if remote_addr is not None and remote_addr == '10.10.1.1':
                return OrderAcceptAction(request.data).run()    
            else:
                return Response(data={'error':'IP is not acceptable','code':406},status=status.HTTP_406_NOT_ACCEPTABLE)