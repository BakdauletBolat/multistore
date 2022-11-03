from django.core.management.base import BaseCommand
from handbook.actions.commands import CreateBrandsAction, CreateCategoriesAction, CreateCitiesAction, \
    CreateDeparmentsAction, CreateQualitiesAction, CreateStoresAction, CreateWareHouseAction

from order.actions.commands import CreateDeliveryMethodAction, CreateOrderStatusAction, CreatePaymentMethodAction
from product.actions.commands import CreateProductsAction, CreatePricesAction
from stock.actions.commands import CreateStocksAction
from users.actions.commands import CreateUserAction


class Command(BaseCommand):
    help = 'Создание данных'

    def handle(self, *args, **options):
        CreateUserAction().run()
        CreateStoresAction().run()
        CreateCategoriesAction().run()
        CreateBrandsAction().run()
        CreateCitiesAction().run()
        CreateDeparmentsAction().run()
        CreateQualitiesAction().run()
        CreateWareHouseAction().run()
        CreateDeliveryMethodAction.run()
        CreateOrderStatusAction.run()
        CreatePaymentMethodAction.run()
        CreateProductsAction().run()
        CreatePricesAction().run()
        # CreateStocksAction().run()
