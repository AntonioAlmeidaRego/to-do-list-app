from django.test import TestCase

# Create your tests here.
from color.models import Color


class ColorTestCase(TestCase):

    def setUp(self):
        self.yellow: Color = Color.objects.create(type_color=1)
        self.blue: Color = Color.objects.create(type_color=2)
        self.gray: Color = Color.objects.create(type_color=3)

    def test_type_colors(self):
        self.assertEqual(self.yellow.type_color, 1)
        self.assertEqual(self.blue.type_color, 2)
        self.assertEqual(self.gray.type_color, 3)
