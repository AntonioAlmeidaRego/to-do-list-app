from django.test import TestCase

# Create your tests here.
from color.models import Color
from model_car.models import ModelCar


class ModelCarTestCase(TestCase):

    def setUp(self):
        self.hatch: ModelCar = ModelCar.objects.create(type_model=1)
        self.sedan: ModelCar = ModelCar.objects.create(type_model=2)
        self.convertible: ModelCar = ModelCar.objects.create(type_model=3)

    def test_type_models(self):
        self.assertEqual(self.hatch.type_model, 1)
        self.assertEqual(self.sedan.type_model, 2)
        self.assertEqual(self.convertible.type_model, 3)
