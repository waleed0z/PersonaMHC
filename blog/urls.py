from django.urls import path
from .views import create_post, read_posts, my_static_page, post_detail
from django.views.generic import TemplateView
urlpatterns = [
    path('', my_static_page, name='index'),
    path('create/', create_post, name='create_post'),
    path('read/', read_posts, name='read_posts'),
    path('post/<int:post_id>/', post_detail, name='post_detail'),
]
