from order.models.OrderStatus import OrderStatus
from order.models.Order import Order
from order.models.OrderItem import OrderItem
from order.models.OrderResponse import OrderResponse
from django.contrib import admin


admin.site.register(Order)
admin.site.register(OrderStatus)
admin.site.register(OrderItem)
admin.site.register(OrderResponse)
