from django.db import models


class Category(models.Model):

    name = models.CharField(max_length=255)
    uid = models.CharField(max_length=255,null=True, blank=True)
    store = models.ForeignKey('store.Store',on_delete=models.CASCADE,null=True,blank=True)
    parent = models.ForeignKey('self',on_delete=models.CASCADE,blank=True,null=True,related_name='categories')
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self)->str:
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категорий'

    