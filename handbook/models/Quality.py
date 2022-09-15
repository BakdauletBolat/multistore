from django.db import models


class Quality(models.Model):

    name = models.CharField(max_length=255)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)


    def __str__(self)->str:
        return self.name

    class Meta:
        verbose_name = 'Качество'
        verbose_name_plural = 'Качествы'
