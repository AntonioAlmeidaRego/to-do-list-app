from django.db import models

# Create your models here.
from car.models import Car
from owner.models import Owner
from utils.models.base_model import BaseModel


class Store(BaseModel):
    name = models.CharField(max_length=255, null=False)
    cars = models.ManyToManyField(Car, blank=False)
    owner = models.ManyToManyField(Owner, blank=False)
