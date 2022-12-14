from django.urls import path
from .views import list, create, update, delete, details

urlpatterns = [
    path('list/', list, name='list_owners'),
    path('create/', create, name='create_owners'),
    path('update/<int:pk>', update, name='update_owners'),
    path('delete/<int:pk>', delete, name='delete_owners'),
    path('details/<int:pk>', details, name='details_owners'),
]
