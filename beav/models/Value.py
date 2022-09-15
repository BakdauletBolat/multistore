from django.db import models


class Value(models.Model):

    name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name

    
    class Meta:
        verbose_name = 'Поля'
        verbose_name_plural = 'Поля'