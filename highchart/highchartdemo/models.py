from django.db import models

# Create your models here.
class Passenger(models.Model):
    name = models.CharField(max_length=120)
    sex = models.CharField(max_length=120)
    survived = models.BooleanField()
    age = models.FloatField()
    pclass = models.PositiveSmallIntegerField()
    embarked = models.CharField(max_length=120)