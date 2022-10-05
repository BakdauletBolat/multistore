from django.urls import path,include
from photo.ui.api.controllers.PhotoCreateController import PhotoCreateController

photo_urlpatterns = [
    path('photo/',include([
        path('create/',PhotoCreateController.as_view())
    ]))
]