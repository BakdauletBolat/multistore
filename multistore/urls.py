
from django.contrib import admin
from django.urls import path, include
from users.ui.api.routes.index import urlpatterns
from product.ui.api.routes.index import urlpatterns_product
from order.ui.api.routes.index import urlpatterns_order
from handbook.ui.api.routes.index import urlpatterns_handbook
from stock.ui.api.routes.index import urlpatterns_stock
from busket.ui.api.routes.index import busket_urlpatterns
from photo.ui.api.routes.index import photo_urlpatterns
from django.conf import settings
from django.conf.urls.static import static


from product.ui.admin.routes.index import urlpatterns_product_admin

urlpatterns = [
    path('api/v1/', include([
        path('admin/',include([
            path('',include(urlpatterns_product_admin))
        ])),
        path('', include(urlpatterns)),
        path('', include(urlpatterns_product)),
        path('', include(urlpatterns_order)),
        path('', include(urlpatterns_handbook)),
        path('', include(urlpatterns_stock)),
        path('',include(busket_urlpatterns)),
        path('',include(photo_urlpatterns))
    ])),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
