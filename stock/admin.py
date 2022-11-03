from stock.models import Stock
from django.contrib import admin


class StockAdmin(admin.ModelAdmin):
    raw_id_fields = ('product',)
    list_filter = ('warehouse',)


admin.site.register(Stock, StockAdmin)
