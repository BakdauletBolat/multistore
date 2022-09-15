from rest_framework import serializers

from busket.models.Busket import Busket
from busket.ui.api.transformers.BusketItemTransformer import BusketItemTransformer

class BusketTransformer(serializers.ModelSerializer):

    items = BusketItemTransformer(many=True)

    class Meta:

        fields = ('__all__')
        model = Busket