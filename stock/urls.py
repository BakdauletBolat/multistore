from django.urls import path, include

from stock.views.api import StockGetView

urlpatterns = [
    path('samsung/', include([
        path('', StockGetView.as_view()),
    ]))
]
