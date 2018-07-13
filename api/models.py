from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator

GENDER_CHOICES = (
    ('M', 'Male'),
    ('F', 'Female')
)


class User(AbstractUser):
    gender = models.CharField(max_length=1, null=True, choices=GENDER_CHOICES)
    birth_date = models.DateField(null=True)
    country = models.CharField(null=True)


class Location(models.Model):
    country = models.CharField()
    city = models.CharField()
    name = models.CharField()
    description = models.CharField()


class Visit(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    date = models.DateTimeField()
    ratio = models.SmallIntegerField(validators=(MinValueValidator(0), MaxValueValidator(10)))
