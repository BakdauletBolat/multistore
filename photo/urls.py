from django.urls import path, include
from photo.views.api import PhotoCreateView


urlpatterns = [
    path('create/', PhotoCreateView.as_view())
]
