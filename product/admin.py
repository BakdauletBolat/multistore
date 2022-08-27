from beav.models.Entity import Entity
from product.models.Product import Product
from django.contrib import admin



class EntityTabularInline(admin.TabularInline):

    model = Entity



class ProductAdmin(admin.ModelAdmin):

    inlines = [EntityTabularInline]
    list_filter = ('store','category')
    list_display = ('id','name','full_name')
    search_fields = ('name','full_name')

    

   

admin.site.register(Product,ProductAdmin)