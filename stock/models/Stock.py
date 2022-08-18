from django.db import models


class Stock(models.Model):

    quality = models.ForeignKey('handbook.Quality',related_name='stocks',on_delete=models.CASCADE)
    store = models.ForeignKey('store.Store',related_name='stocks',on_delete=models.CASCADE)
    wirehouse = models.ForeignKey('handbook.WireHouse',related_name='stocks',on_delete=models.CASCADE)
    category = models.ForeignKey('handbook.Category',related_name='stocks',on_delete=models.CASCADE)
    product = models.ForeignKey('product.Product',related_name='stocks',on_delete=models.CASCADE)
    city = models.ForeignKey('handbook.City',related_name='stocks',on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)