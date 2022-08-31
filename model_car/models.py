from django.db import models

# Create your models here.
from utils.models.base_model import BaseModel
from utils.models.to_str import str_choices_model


class ModelCar(BaseModel):
    HATCH = 1
    SEDAN = 2
    CONVERTIBLE = 3
    MODELS = (
        (HATCH, 'Hatch'),
        (SEDAN, 'Sedan'),
        (CONVERTIBLE, 'Convertible')
    )

    type_model = models.PositiveIntegerField(choices=MODELS, blank=True, null=False)

    def __str__(self):
        return str_choices_model(self)

    class Meta:
        db_table = 'model_cars'
