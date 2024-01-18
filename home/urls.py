from django.urls import path
from .views import my_static_page

urlpatterns = [
    path('', my_static_page, name='index'),

]
