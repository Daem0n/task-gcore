from rest_framework import serializers
from django.conf import settings
from api.models import Location, Visit


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = settings.AUTH_USER_MODEL
        fields = ('id', 'username', 'email', 'first_name', 'last_name', 'gender', 'birth_date', 'country')


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ('id', 'country', 'city', 'name', 'description')


class VisitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Visit
        fields = ('id', 'user_id', 'location_id', 'date', 'ratio')
