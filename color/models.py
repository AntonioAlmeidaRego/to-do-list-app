from django.db import models

# Create your models here.
from utils.models.base_model import BaseModel
from utils.models.to_str import str_choices_color


class Color(BaseModel):
    YELLOW = 1
    BLUE = 2
    GRAY = 3
    COLORS = (
        (YELLOW, 'Yellow'),
        (BLUE, 'Blue'),
        (GRAY, 'gray')
    )

    type_color = models.PositiveIntegerField(choices=COLORS, blank=True, null=False)

    def __str__(self):
        return str_choices_color(self)
