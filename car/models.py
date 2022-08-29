from django.db import models

# Create your models here.
from to_do_list_app.color.models import Color
from to_do_list_app.model_car.models import ModelCar
from to_do_list_app.utils.models.base import BaseModel


class Car(BaseModel):
    name = models.CharField(max_length=255, blank=True, null=False)
    color = models.ForeignKey(Color, on_delete=models.PROTECT, null=False)
    model = models.ForeignKey(ModelCar, on_delete=models.PROTECT, null=False)

    def __str__(self):
        return self.name
