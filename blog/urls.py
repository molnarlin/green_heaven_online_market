from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.blog, name='blog'),
    path('<slug:slug>/', views.posts, name='posts'),
    path('like/<int:post_id>/', views.like_post, name='like_post'),
    path('saved/', views.saved_posts, name='saved_posts'),
]
