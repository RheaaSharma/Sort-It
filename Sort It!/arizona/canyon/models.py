from django.db import models
from django.conf import settings
from django.db import models
from django.db.models import Q
import datetime

# Create your models here.


class Square(models.Model):
    filename = models.CharField(max_length=255)
    coffee = models.CharField(max_length=255, default=None)
    number = models.CharField(max_length=255, default=None)





