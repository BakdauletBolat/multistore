from rest_framework import status,serializers
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.exceptions import ValidationError
from handbook.models.City import City

from stock.models.Stock import Stock
from stock.ui.api.transformers.StockTransformer import StockTransformer




class StockFilterTransformer(serializers.Serializer):
    city_id = serializers.IntegerField()
    product_id = serializers.IntegerField()

class StockGetController(APIView):

    def get(self, request, *args, **kwargs):
        try:
    
            data = StockFilterTransformer(data=request.GET)
            data.is_valid(raise_exception=True)
            wirehouses_ids = City.objects.get(id=data.validated_data['city_id']).warehouses.values_list('id',flat=True)
            print(wirehouses_ids)
            stocks = Stock.objects.filter(wirehouse_id__in=wirehouses_ids,product_id=data.validated_data['product_id'])
        
              
            return Response(data=StockTransformer(stocks,many=True).data,status=status.HTTP_200_OK)
        except ValidationError as e:
            return Response(data=e.get_full_details(),status=e.status_code) 
        except Exception as e:
            return Response(data=str(e),status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def post(self,request):
        try:
            return Response(data={'status':'ok'},status=status.HTTP_200_OK)
        except Exception as e:
            return Response(data=str(e),status=status.HTTP_500_INTERNAL_SERVER_ERROR)