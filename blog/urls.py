from django.urls import path
from .views import create_post, read_posts
from django.views.generic import TemplateView
urlpatterns = [
    path('create/', create_post, name='create_post'),
    path('read/', read_posts, name='read_posts'),
]
