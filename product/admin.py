from beav.models.Entity import Entity
from product.models.Product import Product, ProductBase
from django.contrib import admin



class EntityTabularInline(admin.TabularInline):

    model = Entity



class ProductBaseAdmin(admin.ModelAdmin):

    list_filter = ('category',)
    list_display = ('id','name','full_name')
    list_display_links = ('name',)
    search_fields = ('name','full_name')

    


admin.site.register(ProductBase,ProductBaseAdmin)
admin.site.register(Product)