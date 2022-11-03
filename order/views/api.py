from order.actions.api import OrderAcceptAction
from rest_framework.request import Request

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from order.actions.api import OrderCreateAction
from order.serializers import OrderSerializer
from order.models import Order
from order.utils import get_client_ip


class OrderAcceptView(APIView):
    """Веб контроллер для принятие платежей"""

    def post(self, request: Request) -> Response:

        remote_addr: str = get_client_ip(request)

        if remote_addr is not None and remote_addr == '10.10.1.1':
            order = OrderAcceptAction(request.data).run()
            return Response(data=Order)
        else:
            return Response(data={'error': 'IP is not acceptable', 'code': 406}, status=status.HTTP_406_NOT_ACCEPTABLE)


class OrderCreateView(APIView):
    """Веб контроллер для создание заказа"""

    @staticmethod
    def post(request) -> Response:
        order: Order = OrderCreateAction(data=request.data).run()
        return Response(data=OrderSerializer(order).data, status=status.HTTP_200_OK)
