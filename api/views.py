from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from api.models import User, Location, Visit
from api.serializers import RegisterUserSerializer, \
    UserSerializer, \
    LocationSerializer, \
    LocationRatioSerializer, \
    VisitSerializer
from api.permissions import IsOwnerOrReadOnly, IsSelfOrReadOnly


class UserRegister(APIView):
    """
    Register new user
    """

    def post(self, request, format=None):
        serializer = RegisterUserSerializer(data=request.data)
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
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Get information about user, update it and destroy
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsSelfOrReadOnly,)


class LocationList(generics.ListCreateAPIView):
    """
    List all location and create new one
    """
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class LocationDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Get information about location, update it and destroy
    """
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class LocationVisit(generics.CreateAPIView):
    """
    Visit location
    """
    queryset = Location.objects.all()
    serializer_class = VisitSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user, location=self.get_object())


class LocationRatio(generics.RetrieveAPIView):
    """
    Get ratio for location
    """
    queryset = Location.objects.all()
    serializer_class = LocationRatioSerializer


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
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)


class UserRatio(generics.GenericAPIView):
    """
    Get information user visits
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get(self, request, *args, **kwargs):
        user = self.get_object()
        return Response()
