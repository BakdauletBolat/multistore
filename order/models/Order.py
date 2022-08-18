from django.db import models

class Order(models.Model):


    user = models.ForeignKey('users.User',on_delete=models.CASCADE,verbose_name='Пользователь',related_name='orders')
    status = models.ForeignKey('order.OrderStatus', on_delete=models.CASCADE,verbose_name='Статус заказа',related_name='orders')
    is_paid = models.BooleanField(default=False,verbose_name='Оплачен ?')
    paid_date = models.DateTimeField(null=True,blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)