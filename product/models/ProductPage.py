from django.db import models




class ProductPage(models.Model):

    title = models.CharField(max_length=255,null=True,blank=True)
    description = models.TextField(null=True,blank=True)
    lang = models.ForeignKey('handbook.Language',null=True,blank=True)
    city = models.ForeignKey('handbook.City',null=True,blank=True)
    store = models.ForeignKey('handbook.Store',null=True,blank=True)
    product = models.ForeignKey('product.Product')
