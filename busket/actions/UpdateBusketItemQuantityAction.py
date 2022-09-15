from busket.models.BusketItem import BusketItem
from django.shortcuts import get_object_or_404
from busket.ui.api.transformers.BusketQuantiyUpdateTransformer import BusketQuantiyUpdateTransformer

class UpdateBusketItemQuantityAction:
    """Изменение количество товара"""

    def __init__(self,transformer:BusketQuantiyUpdateTransformer) -> None:
        self.transformer = transformer

    
    def run(self) -> BusketItem:
                
        busket_item = get_object_or_404(BusketItem,id=self.transformer.validated_data.get('busket_item_id')) # type: ignore

        if self.transformer.validated_data.get('quantity') != None: # type: ignore
            busket_item.quantity = self.transformer.validated_data.get('quantity') # type: ignore
        else:
            busket_item.quantity += 1
        
        busket_item.save()

        return busket_item