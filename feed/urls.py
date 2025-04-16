# I M P O R T S   &   D E P E N D E N C I E S ----------------------
from django.urls import path
from .import views

# U R L S ----------------------------------------------------------

# Post urls
"""
    <int:pk> is Djangos build-in identifier (ID) for each entry in a DataBase!
"""
urlpatterns = [
    path('posts/', views.post_list, name='post-list'),
    path('posts/<int:pk>/', views.post_detail, name='post-detail'),
    path('posts/<int:pk>/like/', views.like_post, name='like-post'),
    path('posts/<int:post_id>/comments/', views.post_comments, name='post-comments'),
]
