from django.db import models
from beav.models.Attribute import Attribute
from beav.models.Group import Group
from beav.models.Value import Value
from product.models.Product import Product

class Entity(models.Model):

    values = models.ManyToManyField(Value,related_name='entities')
    attribute = models.ForeignKey(Attribute,related_name='entities',on_delete=models.CASCADE)
    group = models.ForeignKey(Group, related_name='entities',on_delete=models.CASCADE)
    product = models.ForeignKey(Product,related_name='entities',on_delete=models.CASCADE)





