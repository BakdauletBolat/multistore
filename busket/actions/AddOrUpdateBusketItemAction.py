from busket.models.BusketItem import BusketItem
from busket.ui.api.transformers.BusketItemTransformer import BusketCreateTransformer

class AddOrUpdateBuskerItemAction:
    """Добавление товара в корзину или обновить если товар уже есть в корзине"""

    def __init__(self,transformer:BusketCreateTransformer,busket) -> None:
        self.transformer = transformer
        self.busket = busket

    
    def run(self) -> None:        
        filtered = self.busket.items.filter(product_id=self.transformer.validated_data.get('product_id')) #type: ignore
        if len(filtered) > 0:
            item = filtered.first()# type: ignore
            item.quantity += self.transformer.validated_data.get('quantity')# type: ignore
            item.save()
        else:
            BusketItem.objects.create(**self.transformer.validated_data,busket_id=self.busket.id)  # type: ignore