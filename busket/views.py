from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import JsonResponse
from busket.actions.api import GetBusketAction, AddOrUpdateBuskerItemAction, UpdateBusketItemQuantityAction
from busket.tasks.api import GenerateDataToFindSaleAndGetBusketTask
from busket.serializers import BusketSerializer, BusketCreateSerializer, BusketItemSerializer, \
    BusketQuantiyUpdateSerializer
from django.db import transaction
from multistore.request import SaleServiceRequest


class BusketAddItemView(APIView):
    """Веб контроллер для добавление товара на корзину

    """

    @staticmethod
    def post(request) -> JsonResponse | Response:
        with transaction.atomic():
            transformer = BusketCreateSerializer(data=request.data)
            transformer.is_valid(raise_exception=True)
            busket, value_uuid = GetBusketAction().run(request=request)
            AddOrUpdateBuskerItemAction(transformer=transformer, busket=busket).run()
            response = JsonResponse(BusketSerializer(busket).data)

            if value_uuid:
                response.set_cookie('uuid_user', value_uuid)
            return response


class BusketCreateView(APIView):
    """Веб контроллер для создание корзины

    attr: Create
    """

    @staticmethod
    def post(request) -> JsonResponse | Response:
        with transaction.atomic():
            busket, value_uuid = GetBusketAction().run(request=request)
            response = JsonResponse(BusketSerializer(busket).data)

            if value_uuid:
                response.set_cookie('uuid_user', value_uuid)
            return response


class BusketUpdateQuantityView(APIView):
    """Веб контроллер для добавление товара на корзину

    """

    @staticmethod
    def patch(request) -> JsonResponse | Response:
        with transaction.atomic():
            transformer = BusketQuantiyUpdateSerializer(data=request.data)
            transformer.is_valid(raise_exception=True)
            busket_item = UpdateBusketItemQuantityAction(transformer).run()
            return Response(data=BusketItemSerializer(busket_item).data, status=status.HTTP_200_OK)


class BusketUseSalesView(APIView):
    """Веб контроллер для формирования акций
    """



    @staticmethod
    def contains_and_get(items, id):
        for elem in items:
            if elem['busket_item_id'] == id:
                return True, elem
            return False, None

    def get(self, request, pk) -> JsonResponse | Response:
        api = SaleServiceRequest()
        with transaction.atomic():
            data, busket = GenerateDataToFindSaleAndGetBusketTask(pk).run()
            data_return = api.find_sales(data)

            cascades = data_return['data']['cascades']
            others = data_return['data']['others']

            items = []

            for other_item in others:
                is_contain, sale_item = self.contains_and_get(items, other_item['busket_item_id'])
                if is_contain:
                    sale_item['quantity'] += 1
                else:
                    items.append({
                        "product_id": other_item['product']['id'],
                        'new_price': other_item['new_price'],
                        'price': other_item['price'],
                        'busket_item_id': other_item['busket_item_id'],
                        'sales': ', '.join(str(elem['type']) for elem in other_item['sales']),
                        'quantity': 1
                    })

            for cascade in cascades:
                childs = []
                sale_item = {
                    "product_id": cascade['product']['id'],
                    'new_price': cascade['new_price'],
                    'price': cascade['price'],
                    'busket_item_id': cascade['busket_item_id'],
                    'sales': ', '.join(str(elem['type']) for elem in cascade['sales']),
                    'childs': []
                }

                for cascade_item in cascade['childs']:
                    childs.append(
                        {
                            "product_id": cascade_item['product']['id'],
                            'new_price': cascade_item['new_price'],
                            'price': cascade_item['price'],
                            'busket_item_id': cascade_item['busket_item_id'],
                            'sales': ', '.join(str(elem['type']) for elem in cascade_item['sales'])
                        }
                    )

                sale_item['childs'] = childs

                items.append(object)

            return Response(data=items, status=status.HTTP_200_OK)
