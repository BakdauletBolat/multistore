from stock.models.Stock import Stock
from django.contrib import admin



class StockAdmin(admin.ModelAdmin):

    list_filter = ('store',)


admin.site.register(Stock,StockAdmin)