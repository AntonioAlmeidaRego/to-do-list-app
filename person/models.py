from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
from to_do_list_app.utils.models.base import BaseModel


class Person(BaseModel, AbstractUser):
    name = models.CharField(max_length=255, blank=True, null=False)
    email = models.CharField(max_length=255, blank=True, null=False)

