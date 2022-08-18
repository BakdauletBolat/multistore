from django.db import models

class OrderItem(models.Model):

    product = models.ForeignKey('product.Product',related_name='order_items',on_delete=models.CASCADE)
    order = models.ForeignKey('order.Order',related_name='order_items',on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    cost = models.IntegerField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
