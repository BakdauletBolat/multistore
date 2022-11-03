from django.db import models
from order.utils import get_short_uuid


class DeliveryMethod(models.Model):
    name = models.CharField('Название', max_length=255)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = 'Способ доставки'
        verbose_name_plural = 'Способы доставки'


class Address(models.Model):
    city = models.ForeignKey('handbook.City', on_delete=models.CASCADE)
    street = models.CharField(max_length=255)
    number_house = models.CharField(max_length=255)
    number_flat = models.CharField(max_length=255, null=True, blank=True)
    user = models.ForeignKey('users.User', null=True, blank=True, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Адрес'
        verbose_name_plural = 'Адресы'


class Order(models.Model):
    uuid = models.CharField(default=get_short_uuid, null=True, blank=True, unique=True, max_length=10)
    user = models.ForeignKey('users.User', on_delete=models.CASCADE, verbose_name='Пользователь', related_name='orders')
    status = models.ForeignKey('order.OrderStatus', on_delete=models.CASCADE, verbose_name='Статус заказа',
                               related_name='orders')
    is_paid = models.BooleanField(default=False, verbose_name='Оплачен ?')
    paid_date = models.DateTimeField(null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    payment_method = models.ForeignKey('order.PaymentMethod', on_delete=models.CASCADE)
    delivery_method = models.ForeignKey('order.DeliveryMethod', on_delete=models.CASCADE)
    comment = models.TextField(blank=True, null=True)
    shipping_address = models.ForeignKey(Address, on_delete=models.CASCADE, blank=True, null=True,
                                         related_name='order_shipping_address')
    billing_address = models.ForeignKey(Address, on_delete=models.CASCADE, blank=True, null=True,
                                        related_name='order_billing_address')
    store = models.ForeignKey('store.Store', on_delete=models.CASCADE)
    updated_date = models.DateTimeField(auto_now=True)
    operation_id = models.BigIntegerField(default=0)

    def __str__(self) -> str:
        return self.uuid

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'


class OrderItem(models.Model):
    product = models.ForeignKey('product.ProductBase', related_name='order_items', on_delete=models.CASCADE)
    order = models.ForeignKey('order.Order', related_name='order_items', on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    cost = models.IntegerField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.product.name}: qt: {self.quantity} - {self.cost} тг"

    class Meta:
        verbose_name = 'Продукт заказа'
        verbose_name_plural = 'Продукты заказа'


class OrderResponse(models.Model):
    order = models.ForeignKey('order.Order', related_name='order_responses', on_delete=models.CASCADE)
    code = models.CharField(max_length=255)
    amount = models.IntegerField()
    email = models.CharField(max_length=255, null=True, blank=True)
    dateTime = models.DateTimeField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Ответ заказа'
        verbose_name_plural = 'Ответы заказа'


class OrderStatus(models.Model):
    name = models.CharField('Название', max_length=255)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = 'Статус заказа'
        verbose_name_plural = 'Статусы заказа'


class PaymentMethod(models.Model):
    name = models.CharField('Название', max_length=255)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = 'Способ оплаты'
        verbose_name_plural = 'Способы оплаты'
