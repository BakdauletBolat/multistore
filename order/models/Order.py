from django.db import models
from order.utils.get_short_uuid import get_short_uuid

class Order(models.Model):

    uuid = models.CharField(default=get_short_uuid,null=True,blank=True,unique=True,max_length=10)
    user = models.ForeignKey('users.User',on_delete=models.CASCADE,verbose_name='Пользователь',related_name='orders')
    status = models.ForeignKey('order.OrderStatus', on_delete=models.CASCADE,verbose_name='Статус заказа',related_name='orders')
    is_paid = models.BooleanField(default=False,verbose_name='Оплачен ?')
    paid_date = models.DateTimeField(null=True,blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    payment_method = models.ForeignKey('order.PaymentMethod', on_delete=models.CASCADE)
    delivery_method = models.ForeignKey('order.DeliveryMethod',on_delete=models.CASCADE)
    comment = models.TextField(blank=True, null=True)
    shipping_address = models.TextField(blank=True, null=True)
    billing_address = models.TextField(blank=True, null=True) 
    store = models.ForeignKey('store.Store', on_delete=models.CASCADE)
    updated_date = models.DateTimeField(auto_now=True)
    operation_id = models.BigIntegerField(default=0)