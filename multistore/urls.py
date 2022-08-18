
from django.contrib import admin
from django.urls import path,include
from users.ui.api.routes.index import urlpatterns

urlpatterns = [
    path('api/v1/',include([
        path('',include(urlpatterns))
    ])),
    path('admin/', admin.site.urls),
]
