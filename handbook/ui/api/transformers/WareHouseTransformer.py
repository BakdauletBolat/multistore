from rest_framework import serializers
from handbook.models.WareHouse import WareHouse

class WareHouseTransformer(serializers.ModelSerializer):

    class Meta:
        model = WareHouse
        fields = ('__all__')

