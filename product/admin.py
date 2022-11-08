from beav.models import Entity
from product.models import Product, ProductBase, ProductImage, Price, ProductPage
from django.contrib import admin


class EntityTabularInline(admin.TabularInline):
    model = Entity
    raw_id_fields = ['category']


class ProductBaseAdmin(admin.ModelAdmin):
    list_filter = ('category',)
    list_display = ('id', 'name', 'full_name')
    list_display_links = ('name',)
    search_fields = ('name', 'full_name')



class ProductAdmin(admin.ModelAdmin):
    inlines = [EntityTabularInline]
    raw_id_fields = ['base']


admin.site.register(ProductBase, ProductBaseAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(ProductPage)
admin.site.register(ProductImage)
admin.site.register(Price)
