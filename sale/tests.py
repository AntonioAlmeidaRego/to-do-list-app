from django.test import TestCase

# Create your tests here.
from car.models import Car
from color.models import Color
from model_car.models import ModelCar
from owner.models import Owner
from sale.models import Sale
from store.models import Store


class SaleTestCase(TestCase):

    def setUp(self):
        self.store: Store = Store.objects.create(name='CardFord')

        self.pulse: Car = Car.objects.create(name='Pulse', color=Color.objects.create(type_color=1),
                                             model=ModelCar.objects.create(type_model=1))
        self.hilux: Car = Car.objects.create(name='Hilux', color=Color.objects.create(type_color=1),
                                             model=ModelCar.objects.create(type_model=1)
                                             )
        self.onix: Car = Car.objects.create(name='Onix', color=Color.objects.create(type_color=2),
                                            model=ModelCar.objects.create(type_mode=2))

        self.antonio: Owner = Owner.objects.create(name='Antonio', email='antonio.almeida@hotmail.com')
        self.gustavo: Owner = Owner.objects.create(name='Gustavo', email='gustavo.silva@hotmail.com')
        self.fernanda: Owner = Owner.objects.create(name='Fernanda', email='fernanda.sousa@hotmail.com')

        self.sale_antonio: Sale = Sale.objects.create(price=35000, car=self.onix, owner=self.antonio, store=self.store)
        self.sale_justavo: Sale = Sale.objects.create(price=65250, car=self.hilux, owner=self.gustavo, store=self.store)
        self.sale_fernanda: Sale = Sale.objects.create(price=55000, car=self.pulse, owner=self.fernanda,
                                                       store=self.store)

    def test_car(self):
        self.assertEqual(self.sale_antonio.car.name, 'Onix')
        self.assertEqual(self.sale_fernanda.car.name, 'Pulse')
        self.assertEqual(self.sale_justavo.car.name, 'Hilux')
