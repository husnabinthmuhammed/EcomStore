# accounts/urls.py
from django.urls import path
from .views import Register
from .views import UserLogin,TokenRefresh

urlpatterns = [
    path('register/', Register.as_view(), name = 'register'),
    path('login/', UserLogin.as_view(), name='user-login'),
    path('token/refresh/', TokenRefresh.as_view(), name='token-refresh'),
]