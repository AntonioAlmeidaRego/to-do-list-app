from django.db import models

# Create your models here.
from car.models import Car
from utils.models.base_model import BaseModel


class Owner(BaseModel):
    name = models.CharField(max_length=255, blank=True, null=False)
    email = models.CharField(max_length=255, blank=True, null=False)
    cars = models.ManyToManyField(Car, blank=False)

    def __str__(self):
        return self.name
