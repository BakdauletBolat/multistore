from order.models import OrderStatus, DeliveryMethod, PaymentMethod
from loguru import logger


class CreateOrderStatusAction:

    @staticmethod
    def run():
        order_statuses = [
            OrderStatus(
                id=1,
                name='Новый'
            ),
            OrderStatus(
                id=2,
                name='В обработке'
            ),
            OrderStatus(
                id=3,
                name='Возврат'
            ),
            OrderStatus(
                id=4,
                name='Отменен'
            ),
            OrderStatus(
                id=5,
                name='Завершен'
            )
        ]

        OrderStatus.objects.bulk_create(order_statuses,
                                        update_conflicts=True,
                                        unique_fields=['id'],
                                        update_fields=['name'])

        logger.success(f'Успешно импортированы статусы заказа')


class CreateDeliveryMethodAction:

    @staticmethod
    def run():
        order_delivery_methods = [
            DeliveryMethod(
                id=1,
                name='Бесплатная доставка по городу'
            ),
            DeliveryMethod(
                id=2,
                name='Самовывоз из магазина'
            ),
            DeliveryMethod(
                id=3,
                name='Доставка в другой город'
            ),
        ]

        DeliveryMethod.objects.bulk_create(order_delivery_methods,
                                           update_conflicts=True,
                                           unique_fields=['id'],
                                           update_fields=['name'])

        logger.success(f'Успешно импортированы тип доставки')


class CreatePaymentMethodAction:

    @staticmethod
    def run():
        order_payment_methods = [
            PaymentMethod(
                id=1,
                name='Онлайн оплата картой'
            ),
            PaymentMethod(
                id=2,
                name='Оплата при получений'
            )
        ]

        PaymentMethod.objects.bulk_create(order_payment_methods,
                                          update_conflicts=True,
                                          unique_fields=['id'],
                                          update_fields=['name'])

        logger.success(f'Успешно импортированы тип оплаты')
