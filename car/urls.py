from django.urls import path
from .views import list, create, update, delete

urlpatterns = [
    path('list/', list, name='list_cars'),
    path('create/', create, name='create_cars'),
    path('update/<int:pk>', update, name='update_cars'),
    path('delete/<int:pk>', delete, name='delete_cars'),
]
