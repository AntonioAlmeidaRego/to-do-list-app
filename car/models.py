from django.db import models

# Create your models here.
from color.models import Color
from model_car.models import ModelCar
from utils.models.base_model import BaseModel


class Car(BaseModel):
    name = models.CharField(max_length=255, blank=True, null=False)
    color = models.ForeignKey(Color, on_delete=models.PROTECT, null=False)
    model = models.ForeignKey(ModelCar, on_delete=models.PROTECT, null=False)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'cars'
