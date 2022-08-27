from django.db import models

class Product(models.Model):

    name = models.CharField(max_length=255)
    full_name = models.CharField(max_length=255,null=True, blank=True)
    category = models.ForeignKey('handbook.Category',on_delete=models.CASCADE)
    store = models.ForeignKey('store.Store',on_delete=models.CASCADE,null=True,blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    @staticmethod
    def autocomplete_search_fields():
        return ("id__iexact", "name__icontains",)
        