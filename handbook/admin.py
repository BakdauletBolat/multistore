from handbook.models import Category, City, Quality, WareHouse, Language
from django.contrib import admin


class CategoryAdmin(admin.ModelAdmin):
    list_filter = ('stores',)
    list_display = ('id', 'name')


admin.site.register(Category, CategoryAdmin)
admin.site.register(City)
admin.site.register(Quality)


class WareHouseAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'city')
    list_editable = ('city',)


admin.site.register(WareHouse, WareHouseAdmin)
admin.site.register(Language)
