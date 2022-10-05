from django.db import models


class Stock(models.Model):

    quality = models.ForeignKey('handbook.Quality',related_name='stocks',on_delete=models.CASCADE,null=True,blank=True)
    warehouse = models.ForeignKey('handbook.WareHouse',related_name='stocks',on_delete=models.CASCADE,null=True,blank=True)
    product = models.ForeignKey('product.ProductBase',related_name='stocks',on_delete=models.CASCADE,null=True,blank=True)
    city = models.ForeignKey('handbook.City',related_name='stocks',on_delete=models.CASCADE,null=True,blank=True)
    quantity = models.IntegerField(default=1)
    status = models.BooleanField(default=True)
    
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:

        verbose_name = 'Остаток'
        verbose_name_plural = 'Остатьки'