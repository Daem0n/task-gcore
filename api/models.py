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
    country = models.CharField(max_length=256, null=True)


class Location(models.Model):
    country = models.CharField(max_length=256)
    city = models.CharField(max_length=256)
    name = models.CharField(max_length=256)
    description = models.TextField()
    visitors = models.ManyToManyField(User, through='Visit')


# User.locations = models.ManyToManyField(Location, through='Visit')


class Visit(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now=True)
    ratio = models.SmallIntegerField(validators=(MinValueValidator(0), MaxValueValidator(10)))
