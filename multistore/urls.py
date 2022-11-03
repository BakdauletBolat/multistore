from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('api/v1/', include([
        path('beav/', include('beav.urls')),
        path('busket/', include('busket.urls')),
        path('handbook/', include('handbook.urls')),
        path('order/', include('order.urls')),
        path('photo/', include('photo.urls')),
        path('product/', include('product.urls')),
        path('stock/', include('stock.urls')),
        path('store/', include('store.urls')),
        path('users/', include('users.urls'))
    ])),
    path('telemetry/', include('django_telemetry.urls')),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
