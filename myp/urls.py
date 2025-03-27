
from django.contrib import admin
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from users.views import register_user, logout_user, health_check

urlpatterns = [
    path('api/register/', register_user, name='register'),
    path('api/login/', TokenObtainPairView.as_view(), name='login'),
    path('api/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/logout/', logout_user, name='logout'),
    path('api/health/', health_check, name='health_check')

]
