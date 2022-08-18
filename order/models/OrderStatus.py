from django.db import models


class OrderStatus(models.Model):
    name = models.CharField('Название',max_length=255)
    def __str__(self) -> str:
        return self.name