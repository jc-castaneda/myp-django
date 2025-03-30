
from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
import users.views

urlpatterns = [
	path('api/register/', users.views.register_user, name='register'),
    path('api/login/', TokenObtainPairView.as_view(), name='login'),
    path('api/user_info/<int:user_id>', users.views.get_user_info, name='user_info'),
    path('api/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/logout/', users.views.logout_user, name='logout'),
    path('api/health/', users.views.health_check, name='health_check')
]
