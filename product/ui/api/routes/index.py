from django.urls import path,include
from product.ui.api.controllers.samsung.ProductsByCategoryIdController import ProductsByCategoryIdController
from product.ui.api.controllers.samsung.FilterProducts import FilterProductsController

urlpatterns_product = [
    path('samsung/',include([
        path('products/<int:category_id>',ProductsByCategoryIdController.as_view()),
        path('filter/',FilterProductsController.as_view()),
    ]))
]