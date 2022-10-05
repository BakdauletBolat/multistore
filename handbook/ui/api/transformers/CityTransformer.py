from rest_framework import serializers
from handbook.models.City import City

class CityTransformer(serializers.ModelSerializer):
    
    class Meta:

        model = City
        fields = ('id','uid','name')