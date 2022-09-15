import uuid
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import JsonResponse
from busket.actions.CreateAction import GetBusketAction
from busket.ui.api.transformers.Transformer import BusketTransformer
from django.db import transaction

class BusketCreateController(APIView):
    """Веб контроллер для создание корзины

       attr: Create
    """
  
    def post(self,request) -> JsonResponse | Response:

        try:
            with transaction.atomic():
                busket,valueUUID = GetBusketAction().run(request=request)
                response = JsonResponse(BusketTransformer(busket).data,safe=False)

                if valueUUID:
                    response.set_cookie('uuid_user', valueUUID)
                return response
        except Exception as e:
            return Response(data=str(e),status=status.HTTP_500_INTERNAL_SERVER_ERROR)