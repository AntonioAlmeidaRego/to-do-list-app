from django.db import models

# Create your models here.
from car.models import Car
from person.models import Person
from utils.models.base_model import BaseModel


class Owner(BaseModel):
    person = models.ForeignKey(Person, on_delete=models.PROTECT, null=False)
    cars = models.ManyToManyField(Car, blank=False)

    def __str__(self):
        return self.person.name
