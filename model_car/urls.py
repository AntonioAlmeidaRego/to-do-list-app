from django.urls import path
from .views import list, create

urlpatterns = [
    path('list/', list, name='list_models'),
    path('create/', create, name='create_models'),
]
