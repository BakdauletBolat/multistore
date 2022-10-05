from django.core.management.base import BaseCommand
from product.actions.commands import CreateProductsAction


class Command(BaseCommand):
    help = 'Creating Products from IMS'

    def handle(self, *args, **options):
        CreateProductsAction().run()
