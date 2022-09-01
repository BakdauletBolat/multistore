from rest_framework import serializers
from handbook.models.WireHouse import WireHouse

class WireHouseTransformer(serializers.ModelSerializer):

    class Meta:
        model = WireHouse
        fields = ('__all__')

