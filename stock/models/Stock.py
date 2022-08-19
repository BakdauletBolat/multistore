from django.db import models


class Stock(models.Model):

    quality = models.ForeignKey('handbook.Quality',related_name='stocks',on_delete=models.CASCADE,null=True,blank=True)
    store = models.ForeignKey('store.Store',related_name='stocks',on_delete=models.CASCADE,null=True,blank=True)
    wirehouse = models.ForeignKey('handbook.WireHouse',related_name='stocks',on_delete=models.CASCADE,null=True,blank=True)
    product = models.ForeignKey('product.Product',related_name='stocks',on_delete=models.CASCADE,null=True,blank=True)
    city = models.ForeignKey('handbook.City',related_name='stocks',on_delete=models.CASCADE,null=True,blank=True)
    quantity = models.IntegerField(default=1)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)