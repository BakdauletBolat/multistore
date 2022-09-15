from django.db import models


class PaymentMethod(models.Model):
    name = models.CharField('Название',max_length=255)
    def __str__(self) -> str:
        return self.name

    
    class Meta:
        verbose_name = 'Способ оплаты'
        verbose_name_plural = 'Способы оплаты'