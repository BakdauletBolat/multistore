from django.db import models
from handbook.models.City import City

class WireHouse(models.Model):

    name = models.CharField(max_length=255)
    city = models.ForeignKey(City,on_delete=models.CASCADE,null=True,blank=True,related_name='warehouses')
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.name