from rest_framework import serializers

from product.models.Product import Product

class ProductTransformer(serializers.ModelSerializer):
    
    class Meta:
        model = Product
        fields = ('id','name','category_id')
        