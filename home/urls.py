from django.urls import path
from .views import my_static_page, get_educated

urlpatterns = [
    path('', my_static_page, name='index'),
    path('mentinfo', get_educated, name='get_educated'),
]
