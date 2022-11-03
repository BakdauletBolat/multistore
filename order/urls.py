from django.urls import path, include
from order.views.api import OrderAcceptView, OrderCreateView

urlpatterns = [
    path('samsung/', include([
        path('create/', OrderCreateView.as_view()),
        path('accept/', OrderAcceptView.as_view())
    ]))
]
