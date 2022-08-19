from stock.models.Stock import Stock
from store.models.Store import Store
from django.core.management.base import BaseCommand, CommandError
from product.models.Product import Product
from handbook.models.Category import Category
from multistore.request import Request
class Command(BaseCommand):
    help = 'Category create'

    request = Request()
    def handle(self, *args, **options):

        try:
            store = Store.objects.get(id=1)
        except Exception:
            store = Store.objects.create(name='Samsung')

        ids = list(Product.objects.filter(store_id=1).values_list('id', flat=True))

        print(len(ids))
     
        stocks_where_product_samsung = Stock.objects.filter(product_id__in=ids)

        for item in stocks_where_product_samsung:
            item.store_id = store.id
            item.save()

        self.stdout.write(self.style.SUCCESS('Successfully binded Samsung Store products'))