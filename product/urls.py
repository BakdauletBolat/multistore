from django.urls import path, include
from product.views.api import FilterProductsView, ProductsByCategoryIdView
from product.views.admin import ProductListView, ProductDetailView, ProductUploadImageView, ProductGetStockView, \
    GetProductPageView, CreateProductPageView

urlpatterns = [
    path('samsung/', include([
        path('by-category/<int:category_id>/', ProductsByCategoryIdView.as_view()),
        path('filter/<int:pk>/', FilterProductsView.as_view()),
    ])),
    path('admin/', include([
        path('', ProductListView.as_view()),
        path('<int:pk>/', ProductDetailView.as_view()),
        path('upload-image/<int:pk>/', ProductUploadImageView.as_view()),
        path('get-stock/<int:product_id>/<int:quality_id>/', ProductGetStockView.as_view()),
        path('get-product-page/', GetProductPageView.as_view()),
        path('create-product-page/', CreateProductPageView.as_view())
    ]))
]
