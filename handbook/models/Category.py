from django.db import models


class Category(models.Model):

    name = models.CharField(max_length=255)
    store = models.ForeignKey('store.Store',on_delete=models.CASCADE)
    parent = models.ForeignKey('self',on_delete=models.CASCADE,blank=True,null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name