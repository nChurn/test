from django.urls import path

from .views import CreateUserView

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)


urlpatterns = [
    path('signin', TokenObtainPairView.as_view(), name='signin'),
    path('signup', CreateUserView.as_view(), name='signup'),
    path('refresh-token', TokenRefreshView.as_view(), name='token_refresh'),
    
    #path('token-verify', TokenVerifyView.as_view(), name='token_verify'),
]