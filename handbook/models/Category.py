from django.db import models


class Category(models.Model):

    name = models.CharField(max_length=255)
    uid = models.CharField(max_length=255,null=True, blank=True)
    code = models.CharField(max_length=255)
    status = models.BooleanField()
    store = models.ManyToManyField('store.Store')
    parent = models.ForeignKey('self',on_delete=models.CASCADE,blank=True,null=True,related_name='categories')
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self)->str:
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категорий'

    