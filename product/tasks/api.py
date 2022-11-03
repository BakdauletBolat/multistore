from product.models import Product


class GetProductsByCategoryIds:

    def __init__(self, ids) -> None:
        self.ids = ids

    def run(self):
        products = Product.objects.filter(base__category_id__in=self.ids)
        return products
