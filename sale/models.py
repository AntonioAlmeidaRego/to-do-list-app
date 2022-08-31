from django.db import models

# Create your models here.
from car.models import Car
from owner.models import Owner
from store.models import Store
from utils.models.base_model import BaseModel


class Sale(BaseModel):
    price = models.DecimalField(max_length=100, max_digits=10, decimal_places=2)
    car = models.ForeignKey(Car, on_delete=models.PROTECT, null=False)
    owner = models.ForeignKey(Owner, on_delete=models.PROTECT, null=False)
    store = models.ForeignKey(Store, on_delete=models.PROTECT, null=False)

    def __str__(self):
        return f'Preço: R${self.price} | Car: {self.car.name} | P: {self.owner.name}'

    class Meta:
        db_table = 'sales'
