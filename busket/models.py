from django.db import models


class Busket(models.Model):
    uuid_user = models.UUIDField(null=True, blank=True)
    user = models.ForeignKey('users.User', null=True, blank=True, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        if self.user is not None:
            return str(self.user)
        return str(self.uuid_user)

    class Meta:
        verbose_name = "Корзина"


class BusketItem(models.Model):
    product = models.ForeignKey('product.ProductBase', on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    busket = models.ForeignKey('busket.Busket', on_delete=models.CASCADE, related_name='items')
    price = models.IntegerField(default=10)
    sales = models.CharField(max_length=255, null=True, blank=True)
    new_price = models.IntegerField(null=True, blank=True)

    def __str__(self):
        if self.product is not None:
            return self.product.name
        return self.quantity

    class Meta:
        verbose_name = "Элементы корзины"
