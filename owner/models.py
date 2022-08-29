from django.db import models

# Create your models here.
from to_do_list_app.car.models import Car
from to_do_list_app.person.models import Person
from to_do_list_app.utils.models.base import BaseModel


class Owner(BaseModel):
    person = models.ForeignKey(Person, on_delete=models.PROTECT, null=False)
    cars = models.ManyToManyField(Car, blank=False)

    def __str__(self):
        return self.person.name
