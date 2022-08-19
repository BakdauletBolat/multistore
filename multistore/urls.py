
from django.contrib import admin
from django.urls import path, include
from users.ui.api.routes.index import urlpatterns
from product.ui.api.routes.index import urlpatterns_product
from handbook.ui.api.routes.index import urlpatterns_handbook

urlpatterns = [
    path('api/v1/', include([
        path('', include(urlpatterns)),
        path('', include(urlpatterns_product)),
         path('', include(urlpatterns_handbook))
         ])),
    path('admin/', admin.site.urls),
]
