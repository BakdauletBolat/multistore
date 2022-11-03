from loguru import logger
from django.core.management.base import BaseCommand
from product.models import Product, ProductBase

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
            except Exception as _:
                product = Product.objects.create(base=samsung_product)
                product.stores.add(samsung_id)

        logger.success('Привязки товара к самунгу')
