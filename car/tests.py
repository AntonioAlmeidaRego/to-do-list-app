from django.test import TestCase

# Create your tests here.
from car.models import Car
from color.models import Color
from model_car.models import ModelCar


class CarTestCase(TestCase):

    def setUp(self):
        self.pulse: Car = Car.objects.create(name='Pulse', color=Color.objects.create(type_color=1),
                                             model=ModelCar.objects.create(type_model=1))
        self.hilux: Car = Car.objects.create(name='Hilux', color=Color.objects.create(type_color=1),
                                             model=ModelCar.objects.create(type_model=1)
                                             )
        self.onix: Car = Car.objects.create(name='Onix', color=Color.objects.create(type_color=2),
                                            model=ModelCar.objects.create(type_mode=2))

    def test_car(self):
        self.assertEqual(self.pulse.name, 'Pulse')
        self.assertEqual(self.onix.name, 'Onix')
        self.assertEqual(self.hilux.name, 'Hilux')
