from django.db import models

# Create your models here.
from car.models import Car
from owner.models import Owner
from utils.models.base_model import BaseModel


class Store(BaseModel):
    name = models.CharField(max_length=255, null=False)
    cars = models.ManyToManyField(Car, blank=True)
    owners = models.ManyToManyField(Owner, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'stores'
