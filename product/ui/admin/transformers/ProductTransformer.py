from rest_framework import serializers
from handbook.ui.api.transformers.CityTransformer import CityTransformer
from product.models.Product import Product
from itertools import groupby
from operator import itemgetter
from product.ui.api.transformers.ProductBaseTransformer import ProductBaseTransformer
from store.ui.api.transformers.StoreTransformer import StoreTransformer


class ProductTransformer(serializers.ModelSerializer):

    entities = serializers.SerializerMethodField(method_name='get_entities')
    base = ProductBaseTransformer()
    stores = StoreTransformer(many=True)
    cities = CityTransformer(many=True)

    def get_entities(self,obj):
        items = []
        items = obj.entities.values('group__name', 'attribute__name', 'values__name').order_by('group__name')
        rows = groupby(items, itemgetter('group__name'))
        objects = []

        for c_title,items in rows:
            objects.append({
                'group_name': c_title,
                'items': list(items),
            })
       
        return objects
  
    class Meta:
        model = Product
        fields = ('id','base','cities','stores','entities')
