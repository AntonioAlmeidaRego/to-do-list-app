from django.db import models

# Create your models here.
from to_do_list_app.car.models import Car
from to_do_list_app.owner.models import Owner
from to_do_list_app.utils.models.base import BaseModel


class Store(BaseModel):
    name = models.CharField(max_length=255, null=False)
    cars = models.ManyToManyField(Car, blank=False)
    owner = models.ManyToManyField(Owner, blank=False)
