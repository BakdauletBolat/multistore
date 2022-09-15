from django.contrib import admin

from busket.models.Busket import Busket
from busket.models.BusketItem import BusketItem


admin.site.register(Busket)
admin.site.register(BusketItem)