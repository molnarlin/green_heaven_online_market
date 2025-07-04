from django.urls import path
from . import views
from .views import CommentUpdateView
from .views import CommentDeleteView


app_name = 'blog'
urlpatterns = [
    path('', views.post_list, name='post_list'),
    path(
        '<int:year>/<int:month>/<int:day>/<slug:slug>/',
        views.post_detail,
        name='post_detail',
    ),
    path('<int:post_id>/comment/', views.post_comment, name='post_comment'),
    path(
        'comment/<int:pk>/edit/',
        CommentUpdateView.as_view(),
        name='comment_edit'
    ),
    path(
        'comment/<int:pk>/delete/',
        CommentDeleteView.as_view(),
        name='comment_delete'
    ),

]
