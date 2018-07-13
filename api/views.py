from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from api.models import User, Location, Visit
from api.serializers import UserSerializer, LocationSerializer, VisitSerializer


class UserRegister(APIView):
    """
    Register new user
    """

    def post(self, request, format=None):
        serializer = UserSerializer(data=request.date)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserSignIn(generics.GenericAPIView):
    """
    SignIn user
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def post(self, request, format=None):
        return Response()


class UserList(generics.ListAPIView):
    """
    List all users
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Get information about user, update it and destroy
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class LocationList(generics.ListCreateAPIView):
    """
    List all location and create new one
    """
    queryset = Location.objects.all()
    serializer_class = LocationSerializer


class LocationDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Get information about location, update it and destroy
    """
    queryset = Location.objects.all()
    serializer_class = LocationSerializer


class LocationVisit(generics.GenericAPIView):
    """
    Visit location
    """
    queryset = Location.objects.all()
    serializer_class = LocationSerializer

    def post(self, request, format=None):
        location = self.get_object()
        return Response()


class LocationRatio(generics.GenericAPIView):
    """
    Get ratio for location
    """
    queryset = Location.objects.all()
    serializer_class = LocationSerializer

    def get(self, request, format=None):
        location = self.get_object()
        return Response()


class VisitList(generics.ListAPIView):
    """
    List all visits
    """
    queryset = Visit.objects.all()
    serializer_class = VisitSerializer


class VisitDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Get information about visit, update it and destroy
    """
    queryset = Visit.objects.all()
    serializer_class = VisitSerializer


class UserRatio(generics.GenericAPIView):
    """
    Get information user visits
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
