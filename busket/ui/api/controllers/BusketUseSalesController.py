from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import JsonResponse
from django.db import transaction
from busket.tasks.GenerateDataToFindSaleAndGetBusketTask import GenerateDataToFindSaleAndGetBusketTask
from rest_framework.exceptions import ValidationError
from multistore.core.Request import Request


class BusketUseSalesController(APIView):
    """Веб контроллер для формирования акций
    """

    api = Request()
    

    def contains_and_get(self,items,id):
        for elem in items:
            if elem['busket_item_id'] == id:
                return True,elem
        return False,None

    def get(self, request, pk) -> JsonResponse | Response:

        try:
            with transaction.atomic():
                data, busket = GenerateDataToFindSaleAndGetBusketTask(pk).run()
                data_return = self.api.findSales(data)

                cascades = data_return['data']['cascades']
                others = data_return['data']['others']

                items = []

                for other_item in others:
                    is_contain,object = self.contains_and_get(items,other_item['busket_item_id'])
                    if is_contain:
                        object['quantity'] += 1
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
                    object = {
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
                    
                    object['childs'] = childs

                    items.append(object)

                return Response(data=items, status=status.HTTP_200_OK)
        except ValidationError as e:
            return Response(data=e.get_full_details(), status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        except Exception as e:
            return Response(data=str(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR)
