from loguru import logger
from store.models.Store import Store
from django.core.management.base import BaseCommand, CommandError
from product.models.Product import Product, ProductBase
from handbook.models.Category import Category
from multistore.request import Request
class Command(BaseCommand):
    help = 'Category create'

    request = Request()
    def handle(self, *args, **options):
        samsung_id = 4
        samsung_products = ProductBase.objects.filter(brand_id=3)
        

        for samsung_product in samsung_products:
            try:
                product = Product.objects.get(base_id=samsung_product.id)
                product.stores.add(samsung_id)
            except Exception as e:
                product = Product.objects.create(base=samsung_product)
                product.stores.add(samsung_id)

    

        logger.success('Successfully binded Samsung Store products')