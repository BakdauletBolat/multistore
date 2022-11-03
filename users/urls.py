from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from users.views.api import AuthorizationUserView, VerifyUserView

urlpatterns = [
    path('token/', TokenObtainPairView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view()),
    path('authorization/', AuthorizationUserView.as_view()),
    path('verify-otp/', VerifyUserView.as_view())
]
