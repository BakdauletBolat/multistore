from django.core.management.base import BaseCommand
from multistore.request import Request
from order.actions.commands import CreateDeliveryMethodAction, CreateOrderStatusAction, CreatePaymentMethodAction


class Command(BaseCommand):
    help = 'WareHouse create'

    request = Request()

    def handle(self, *args, **options):
        CreateDeliveryMethodAction.run()
        CreateOrderStatusAction.run()
        CreatePaymentMethodAction.run()
