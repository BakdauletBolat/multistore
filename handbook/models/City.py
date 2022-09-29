from django.db import models


class City(models.Model):

    name = models.CharField(max_length=255)
    uid = models.CharField(max_length=255,null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)


    def __str__(self) -> str:
        return f"{self.id} {self.name}"  # type: ignore

    class Meta:
        verbose_name = 'Город'
        verbose_name_plural = 'Города'
