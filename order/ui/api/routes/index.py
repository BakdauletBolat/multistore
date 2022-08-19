from django.urls import path,include
from order.ui.api.controllers.OrderCreateController import OrderCreateController
from order.ui.api.controllers.OrderAcceptController import OrderAcceptController

urlpatterns_order = [
    path('order/',include([
        path('samsung/',include([
            path('create/',OrderCreateController.as_view()),
            path('accept/',OrderAcceptController.as_view())
        ]))
    ]))
]