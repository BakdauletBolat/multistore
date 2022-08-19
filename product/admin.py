from product.models.Product import Product
from django.contrib import admin


class ProductAdmin(admin.ModelAdmin):

    list_filter = ('store',)
    list_display = ('id','name')

admin.site.register(Product,ProductAdmin)