from django.test import TestCase

# Create your tests here.
from car.models import Car
from color.models import Color
from model_car.models import ModelCar
from owner.models import Owner


class OwnerTestCase(TestCase):

    def setUp(self):
        self.antonio: Owner = Owner.objects.create(name='Antonio', email='antonio.almeida@hotmail.com')
        self.gustavo: Owner = Owner.objects.create(name='Gustavo', email='gustavo.silva@hotmail.com')
        self.fernanda: Owner = Owner.objects.create(name='Fernanda', email='fernanda.sousa@hotmail.com')

    def test_car(self):
        self.assertEqual(self.antonio.name, 'Antonio')
        self.assertEqual(self.gustavo.name, 'Gustavo')
        self.assertEqual(self.fernanda.name, 'Fernanda')
