from django.shortcuts import get_object_or_404
from busket.models.Busket import Busket


class GenerateDataToFindSaleAndGetBusketTask:
    """Таск для генерация из корзины на экшен FindSale и возвращает корзину"""

    def __init__(self, pk, payment_method_id=1, shop_id=1):
        self.pk = pk
        self.payment_method_id = payment_method_id
        self.shop_id = shop_id
        self.data = {
            "data": {
                "type": "SaleFind",
                "attributes": {
                    "shop_id": shop_id,
                    "payment_method_id": payment_method_id,
                    "products": []
                }
            }
        }

    def run(self):
        busket = get_object_or_404(Busket,id=self.pk)
        products = []

        for busket_item in busket.items.all():
            products.append(
                {
                    'busket_item_id': busket_item.id,
                    'product_id': busket_item.product.id,
                    'quantity': busket_item.quantity
                }
            )

        self.data['data']['attributes']['products'] = products



        return self.data,busket
