from rest_framework.response import Response
from rest_framework.views import APIView
from handbook.models import City
from stock.models import Stock
from rest_framework import status
from stock.serializers import StockFilterSerializer, StockSerializer


class StockGetView(APIView):

    @staticmethod
    def get(request, *args, **kwargs):
        data = StockFilterSerializer(data=request.GET)
        data.is_valid(raise_exception=True)
        warehouses_ids = City.objects.get(id=data.validated_data['city_id']).warehouses.values_list('id', flat=True)
        stocks = Stock.objects.filter(WareHouse_id__in=warehouses_ids, product_id=data.validated_data['product_id'])
        return Response(data=StockSerializer(stocks, many=True).data, status=status.HTTP_200_OK)
