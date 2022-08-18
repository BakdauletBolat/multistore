from handbook.models.Category import Category
from handbook.models.City import City

from handbook.models.Quality import Quality
from handbook.models.WireHouse import WireHouse
from django.contrib import admin


admin.site.register(Category)
admin.site.register(City)
admin.site.register(Quality)
admin.site.register(WireHouse)