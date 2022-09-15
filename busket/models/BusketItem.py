from django.db import models


class BusketItem(models.Model):

    product = models.ForeignKey('product.Product',on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    busket = models.ForeignKey('busket.Busket',on_delete=models.CASCADE,related_name='items')
    price = models.IntegerField(default=10)
    sales = models.CharField(max_length=255,null=True,blank=True)
    new_price = models.IntegerField(null=True,blank=True)


    def __str__(self):
        if self.product is not None:
            return self.product.name
        return self.quantity

    class Meta:

        verbose_name = "Элементы корзины"