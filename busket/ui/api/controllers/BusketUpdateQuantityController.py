from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import JsonResponse
from busket.actions.AddOrUpdateBusketItemAction import AddOrUpdateBuskerItemAction
from busket.actions.CreateAction import GetBusketAction
from busket.actions.UpdateBusketItemQuantityAction import UpdateBusketItemQuantityAction
from busket.ui.api.transformers.BusketItemTransformer import BusketCreateTransformer, BusketItemTransformer
from busket.ui.api.transformers.BusketQuantiyUpdateTransformer import BusketQuantiyUpdateTransformer
from busket.ui.api.transformers.Transformer import BusketTransformer
from rest_framework.exceptions import ValidationError
from django.db import transaction

class BusketUpdateQuantityController(APIView):
    """Веб контроллер для добавление товара на корзину

    """
  
    def post(self,request) -> JsonResponse | Response:

        try:
            with transaction.atomic():
                transformer = BusketQuantiyUpdateTransformer(data=request.data)
                transformer.is_valid(raise_exception=True)
                busket_item = UpdateBusketItemQuantityAction(transformer).run()
                
                return Response(data=BusketItemTransformer(busket_item).data,status=status.HTTP_200_OK)
        except ValidationError as e:
            return Response(data=e.get_full_details(),status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        except Exception as e:
            return Response(data=str(e),status=status.HTTP_500_INTERNAL_SERVER_ERROR)