from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.db.models import Avg
from api.models import Location, Visit

UserModel = get_user_model()


class RegisterUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = UserModel
        fields = ('id', 'username', 'email', 'first_name', 'last_name', 'password', 'gender', 'birth_date', 'country')

    def create(self, validated_data):
        user = UserModel.objects.create(
            username=validated_data.get('username'),
            email=validated_data.get('email'),
            first_name=validated_data.get('first_name', ''),
            last_name=validated_data.get('last_name', ''),
            gender=validated_data.get('gender'),
            birth_date=validated_data.get('birth_date'),
            country=validated_data.get('country'),
        )
        user.set_password(validated_data.get('password'))
        user.save()
        return user


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = get_user_model()
        fields = ('id', 'username', 'email', 'first_name', 'last_name', 'gender', 'birth_date', 'country')


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ('id', 'country', 'city', 'name', 'description')


class VisitSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    location = serializers.ReadOnlyField(source='location.name')

    class Meta:
        model = Visit
        fields = ('id', 'user_id', 'user', 'location_id', 'location', 'date', 'ratio')


class LocationRatioSerializer(serializers.ModelSerializer):
    count = serializers.SerializerMethodField()
    avg = serializers.SerializerMethodField()
    visitors = VisitSerializer(many=True, read_only=True, source='visit_set')

    class Meta:
        model = Location
        fields = ('count', 'avg', 'visitors')

    def get_count(self, obj):
        count = obj.visit_set.count()
        if count is None:
            return 0
        return count

    def get_avg(self, obj):
        average = obj.visit_set.aggregate(Avg('ratio')).get('ratio__avg')
        if average is None:
            return 0
        return average


class UserRatioSerializer(serializers.ModelSerializer):
    count = serializers.SerializerMethodField()
    avg = serializers.SerializerMethodField()
    locations = VisitSerializer(many=True, read_only=True, source='visit_set')

    class Meta:
        model = UserModel
        fields = ('count', 'avg', 'locations')

    def get_count(self, obj):
        count = obj.visit_set.count()
        if count is None:
            return 0
        return count

    def get_avg(self, obj):
        average = obj.visit_set.aggregate(Avg('ratio')).get('ratio__avg')
        if average is None:
            return 0
        return average
