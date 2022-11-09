from django.core.management.base import BaseCommand
from multistore.celery import app
from product.actions.commands import CreateProductsAction


class CreateProductTask(app.Task):
    name = 'create_products'

    def run(self):
        CreateProductsAction().run()


tas_a = app.register_task(CreateProductTask())


class Command(BaseCommand):
    help = 'Создание продуктов'

    def handle(self, *args, **options):
        tas_a.delay()
