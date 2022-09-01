from stock.models.Stock import Stock
from django.contrib import admin





class StockAdmin(admin.ModelAdmin):
    raw_id_fields = ('product',)
    list_filter = ('store','wirehouse',)


admin.site.register(Stock,StockAdmin)