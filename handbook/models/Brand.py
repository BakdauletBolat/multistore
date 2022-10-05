from django.db import models


class Brand(models.Model):

    name = models.CharField(max_length=255)
    uid = models.CharField(max_length=255,null=True, blank=True)
    code = models.CharField(max_length=255)
    status = models.BooleanField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)


    def __str__(self)->str:
        return f"{self.id}: {self.name}"

    class Meta:
        verbose_name = 'Качество'
        verbose_name_plural = 'Качествы'
