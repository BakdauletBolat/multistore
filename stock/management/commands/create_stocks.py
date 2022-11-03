from django.core.management.base import BaseCommand
from stock.actions.commands import CreateStocksAction


class Command(BaseCommand):
    help = 'Импорт складов IMS'

    def handle(self, *args, **options):
        CreateStocksAction().run()
