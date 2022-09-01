from django.urls import path,include

from stock.ui.api.controllers.StockGetController import StockGetController


urlpatterns_stock = [
    path('stock/',include([
        path('samsung/',include([
            path('',StockGetController.as_view()),
        ]))
    ]))
]