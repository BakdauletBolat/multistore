from django.core.management.base import BaseCommand, CommandError
from order.models.OrderStatus import OrderStatus
from order.models.PaymentMethod import PaymentMethod
from order.models.DeliveryMethod import DeliveryMethod

from multistore.request import Request
class Command(BaseCommand):
    help = 'WareHouse create'

    request = Request()
    def handle(self, *args, **options):


        orderStatuses = [
            OrderStatus(
                name='Новый'
            ),
            OrderStatus(
                name='В обработке'
            ),
            OrderStatus(
                name='Возврат'
            ),
            OrderStatus(
                name='Отменен'
            )
            ,OrderStatus(
                name='Завершен'
            )
        ]


        order_delivery_methods = [
            DeliveryMethod(
                name='Бесплатная доставка по городу'
            ),
            DeliveryMethod(
                name='Самовывоз из магазина'
            ),
            DeliveryMethod(
                name='Доставка в другой город'
            ), 
        ]

        order_payment_methods = [
            PaymentMethod(
                name='Онлайн оплата картой'
            ),
            PaymentMethod(
                name='Оплата при получений'
            )
        ]
        
        OrderStatus.objects.bulk_create(orderStatuses)

        self.stdout.write(self.style.SUCCESS('1. Successfully created order statuses'))

        PaymentMethod.objects.bulk_create(order_payment_methods)

        self.stdout.write(self.style.SUCCESS('2. Successfully created order payment_method'))

        DeliveryMethod.objects.bulk_create(order_delivery_methods)

        self.stdout.write(self.style.SUCCESS('3. Successfully created order delivery_method'))
