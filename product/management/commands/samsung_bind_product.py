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

        ids = list(Category.objects.filter(name='Samsung').values_list('id', flat=True))
     
        products_where_category_samsung = Product.objects.filter(category_id__in=ids)

        for item in products_where_category_samsung:
            item.store_id = store.id
            item.save()

        self.stdout.write(self.style.SUCCESS('Successfully binded Samsung Store products'))