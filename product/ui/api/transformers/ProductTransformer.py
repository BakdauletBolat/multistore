from html import entities
from rest_framework import serializers

from product.models.Product import Product
from itertools import groupby
from operator import itemgetter
from handbook.models.Category import Category

class ProductTransformer(serializers.ModelSerializer):

    entities = serializers.SerializerMethodField(method_name='get_entities')


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
        fields = ('id','name','category_id','full_name','entities')
        