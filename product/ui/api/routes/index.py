from django.urls import path,include
from product.ui.api.controllers.samsung.ProductsByCategoryIdController import ProductsByCategoryIdController

urlpatterns_product = [
    path('samsung/',include([
        path('products/<int:category_id>',ProductsByCategoryIdController.as_view())
    ]))
]