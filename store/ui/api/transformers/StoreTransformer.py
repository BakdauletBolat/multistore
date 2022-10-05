from rest_framework import serializers
from store.models.Store import Store

class StoreTransformer(serializers.ModelSerializer):
    
    class Meta:

        model = Store
        fields = ('id','name')