from django.urls import path, include
from busket.ui.api.controllers.BusketCreateController import BusketCreateController
from busket.ui.api.controllers.BusketAddItemController import BusketAddItemController
from busket.ui.api.controllers.BusketUpdateQuantityController import BusketUpdateQuantityController
from busket.ui.api.controllers.BusketUseSalesController import BusketUseSalesController

busket_urlpatterns = [
    path('busket/', include([
        path('samsung/', include([
            path('get/', BusketCreateController.as_view()),
            path('add-item/',BusketAddItemController.as_view()),
            path('update-item/',BusketUpdateQuantityController.as_view()),
            path('use-sale/<int:pk>/',BusketUseSalesController.as_view())
        ]))
    ]))
]
