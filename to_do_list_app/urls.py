"""to_do_list_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from pages import urls as pages_urls
from color import urls as colors_urls
from model_car import urls as models_urls
from owner import urls as owners_urls
from sale import urls as sales_urls
from car import urls as cars_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(pages_urls)),
    path('colors/', include(colors_urls)),
    path('cars/', include(cars_urls)),
    path('models/', include(models_urls)),
    path('owners/', include(owners_urls)),
    path('sales/', include(sales_urls)),
]
