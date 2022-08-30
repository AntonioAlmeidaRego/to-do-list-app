from django.urls import path
from .views import list, create

urlpatterns = [
    path('list/', list, name='list_colors'),
    path('create/', create, name='create_colors'),
]
