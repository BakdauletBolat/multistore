from handbook.models.Category import Category
from handbook.models.City import City

from handbook.models.Quality import Quality
from handbook.models.WireHouse import WireHouse
from django.contrib import admin



class CategoryAdmin(admin.ModelAdmin):

    list_filter = ('store',)
    list_display = ('id','name')

admin.site.register(Category,CategoryAdmin)
admin.site.register(City)
admin.site.register(Quality)



class WireHouseAdmin(admin.ModelAdmin):
    list_display = ('id','name','city')
    list_editable = ('city',)

admin.site.register(WireHouse,WireHouseAdmin)