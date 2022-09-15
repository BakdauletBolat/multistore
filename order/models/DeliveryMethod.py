from django.db import models


class DeliveryMethod(models.Model):
    name = models.CharField('Название',max_length=255)

    def __str__(self) -> str:
        return self.name
    

    class Meta:
        verbose_name = 'Способ доставки'
        verbose_name_plural = 'Способы доставки'
