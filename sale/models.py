from django.db import models

# Create your models here.
from to_do_list_app.car.models import Car
from to_do_list_app.owner.models import Owner
from to_do_list_app.store.models import Store
from to_do_list_app.utils.models.base import BaseModel


class Sale(BaseModel):
    price = models.DecimalField(max_length=100)
    car = models.ForeignKey(Car, on_delete=models.PROTECT, null=False)
    owner = models.ForeignKey(Owner, on_delete=models.PROTECT, null=False)
    store = models.ForeignKey(Store, on_delete=models.PROTECT, null=False)
