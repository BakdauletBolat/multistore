from busket.models import BusketItem, Busket
from typing import Optional
from busket.serializers import BusketCreateSerializer, BusketQuantiyUpdateSerializer
import uuid
from django.shortcuts import get_object_or_404


class AddOrUpdateBuskerItemAction:
    """Добавление товара в корзину или обновить если товар уже есть в корзине"""

    def __init__(self, transformer: BusketCreateSerializer, busket) -> None:
        self.transformer = transformer
        self.busket = busket

    def run(self) -> None:
        filtered = self.busket.items.filter(product_id=self.transformer.validated_data.get('product_id'))
        if len(filtered) > 0:
            item = filtered.first()
            item.quantity += self.transformer.validated_data.get('quantity')
            item.save()
        else:
            BusketItem.objects.create(**self.transformer.validated_data, busket_id=self.busket.id)


class GetBusketAction:

    def run(self, request) -> tuple[Optional[Busket], str | None]:
        value_uuid = None

        if request.user.is_authenticated:
            try:
                busket = Busket.objects.get(user=request.user, is_active=True)
            except Busket.DoesNotExist:
                busket = Busket.objects.create(user=request.user)
        else:
            uuid_user = request.COOKIES.get('uuid_user', None)
            if uuid_user is not None:
                value = request.COOKIES.get('uuid_user')
                try:
                    busket = Busket.objects.get(uuid_user=value, is_active=True)
                except Busket.DoesNotExist:
                    busket = Busket.objects.create(uuid_user=value)
            else:
                value_uuid = str(uuid.uuid4())
                try:
                    busket = Busket.objects.get(uuid_user=value_uuid, is_active=True)
                except Busket.DoesNotExist:
                    busket = Busket.objects.create(uuid_user=value_uuid)
        return busket, value_uuid


class UpdateBusketItemQuantityAction:
    """Изменение количество товара"""

    def __init__(self, transformer: BusketQuantiyUpdateSerializer) -> None:
        self.transformer = transformer

    def run(self) -> BusketItem:

        busket_item = get_object_or_404(BusketItem,
                                        id=self.transformer.validated_data.get('busket_item_id'))

        if self.transformer.validated_data.get('quantity') is not None:
            busket_item.quantity = self.transformer.validated_data.get('quantity')
        else:
            busket_item.quantity += 1

        busket_item.save()

        return busket_item
