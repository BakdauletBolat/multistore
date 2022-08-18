from django.db import models


class OrderResponse(models.Model):

    order = models.ForeignKey('order.Order',related_name='order_responses',on_delete=models.CASCADE)
    code = models.IntegerField()
    amount = models.IntegerField()
    email = models.CharField(max_length=255,null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    