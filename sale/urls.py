from django.urls import path
from .views import list, create, update, delete

urlpatterns = [
    path('list/', list, name='list_sales'),
    path('create/', create, name='create_sales'),
    path('update/<int:pk>', update, name='update_sales'),
    path('delete/<int:pk>', delete, name='delete_sales'),
]
