from rest_framework import serializers
from stock.models.Stock import Stock
from product.ui.api.transformers.ProductBaseTransformer import ProductBaseTransformer
from handbook.ui.api.transformers.WareHouseTransformer import WareHouseTransformer

class StockTransformer(serializers.ModelSerializer):
    product = ProductBaseTransformer()
    WareHouse = WareHouseTransformer()
    class Meta:
        model = Stock
        fields = ('id','quality','store','WareHouse','product','quantity')