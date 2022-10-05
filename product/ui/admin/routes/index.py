from django.urls import path,include
from product.ui.admin.controllers.ProductListController import ProductListController

urlpatterns_product_admin = [
    path('products/',include([
        path('',ProductListController.as_view()),
    ]))
]