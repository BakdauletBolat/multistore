from rest_framework import serializers
from stock.models.Stock import Stock
from product.ui.api.transformers.ProductTransformer import ProductTransformer
from handbook.ui.api.transformers.WireHouseTransformer import WireHouseTransformer

class StockTransformer(serializers.ModelSerializer):
    product = ProductTransformer()
    wirehouse = WireHouseTransformer()
    class Meta:
        model = Stock
        fields = ('id','quality','store','wirehouse','product','quantity')