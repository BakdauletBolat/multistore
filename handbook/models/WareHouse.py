from django.db import models
from handbook.models.City import City

class WareHouse(models.Model):

    name = models.CharField(max_length=255)
    uid = models.CharField(max_length=255,null=True, blank=True)
    code = models.CharField(max_length=255)
    status = models.BooleanField()
    store = models.ForeignKey('store.Store',on_delete=models.CASCADE,null=True,blank=True,related_name='warehouses')
    city = models.ForeignKey(City,on_delete=models.CASCADE,null=True,blank=True,related_name='warehouses')
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)


    def __str__(self)->str:
        return self.name
    

    class Meta:
        verbose_name = 'Склад'
        verbose_name_plural = 'Склады'
