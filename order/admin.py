from order.models import Order, OrderItem, OrderStatus, OrderResponse, DeliveryMethod, PaymentMethod
from django.contrib import admin


admin.site.register(Order)
admin.site.register(OrderStatus)
admin.site.register(OrderItem)
admin.site.register(OrderResponse)
admin.site.register(DeliveryMethod)
admin.site.register(PaymentMethod)
