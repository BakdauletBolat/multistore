from django.db import models


class Quality(models.Model):

    name = models.CharField(max_length=255)
    uid = models.CharField(max_length=255,null=True, blank=True)
    code = models.CharField(max_length=255)
    status = models.BooleanField()
    alias = models.CharField(max_length=255)
    order = models.IntegerField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)


    def __str__(self)->str:
        return self.name

    class Meta:
        verbose_name = 'Качество'
        verbose_name_plural = 'Качествы'
