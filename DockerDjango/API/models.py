from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import DecimalField, PositiveSmallIntegerField
from django.db.models.fields.related import ForeignKey
from django.contrib.auth.models import User

# Create your models here.

class Restaurant(models.Model):
    name = models.CharField(max_length=200)
    latitude = DecimalField(max_digits=9, decimal_places=6)
    longitude = DecimalField(max_digits=9, decimal_places=6)
    rating = PositiveSmallIntegerField()
    author = ForeignKey(User, on_delete=CASCADE)

    def __str__(self):
        return self.name