from django.urls import path, include
from busket.views import BusketAddItemView, BusketCreateView, BusketUpdateQuantityView, BusketUseSalesView

urlpatterns = [
    path('samsung/', include([
        path('get/', BusketCreateView.as_view()),
        path('add-item/', BusketAddItemView.as_view()),
        path('update-item/', BusketUpdateQuantityView.as_view()),
        path('use-sale/<int:pk>/', BusketUseSalesView.as_view())
    ]))
]
