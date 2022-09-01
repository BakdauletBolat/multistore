
from django.contrib import admin
from django.urls import path, include
from users.ui.api.routes.index import urlpatterns
from product.ui.api.routes.index import urlpatterns_product
from order.ui.api.routes.index import urlpatterns_order
from handbook.ui.api.routes.index import urlpatterns_handbook
from stock.ui.api.routes.index import urlpatterns_stock
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('grappelli/', include('grappelli.urls')),
    path('api/v1/', include([
        path('', include(urlpatterns)),
        path('', include(urlpatterns_product)),
        path('', include(urlpatterns_order)),
        path('', include(urlpatterns_handbook)),
        path('', include(urlpatterns_stock))
    ])),
    path('admin/', admin.site.urls),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
