from rest_framework import serializers

from product.models.Product import ProductBase

class ProductBaseTransformer(serializers.ModelSerializer):

    class Meta:
        model = ProductBase
        fields = ('id','name','category_id','full_name')
        