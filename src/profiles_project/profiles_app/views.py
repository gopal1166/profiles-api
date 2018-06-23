from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import HttpResponse
from . import serializers
from .serializers import TestSerializer, UserProfileSerializer, ProfileFeedSerializer
from .models import UserProfile, ProfileFeed
from . import models


from rest_framework.authentication import TokenAuthentication
from .permissions import UpdateOwnProfile, UpdateOwnProfileFeed
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework import filters

from rest_framework import viewsets

from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authtoken.views import ObtainAuthToken

# Create your views here.
class TestApiView(APIView):
    """Testing our first ApiView
        ApiView uses Http methods as functions"""

    serializer_class = serializers.TestSerializer

    def get(self, request, format=None):
        """Returns simple success message"""

        return Response({'stats': 'success', 'message': 'Bello ApiView is working'})

    def post(self, request):

        mySerializer = serializers.TestSerializer(data=request.data)

        if mySerializer.is_valid():
            myName = mySerializer.data.get('name')
            message = 'Bello {0}'.format(myName)

            return Response({'status': 'success', 'message': message})

    def put(self, request, pk=None):
        """Updates an object"""

        return Response({'status': 'success', 'method': 'put'})

    def patch(self, request, pk=None):
        """Partially updates an object: Only updates fields provided in request"""

        return Response({'status': 'success', 'method': 'patch'})

    def delete(self, request, pk=None):
        """Deletes an object """

        return Response({'status': 'success', 'method': 'delete'})


class TestViewSet(viewsets.ViewSet):
    """First ViewSet"""

    def list(self, request):
        """Returns a list """

        myList = ['Gopa', 'Ram']
        return Response({'method': 'list', 'list': myList})

    def create(self, request):
        """Creates an object """

        serializer = TestSerializer(data=request.data)

        if serializer.is_valid():
            name = serializer.data.get('name')
            message = 'Bello {0}'.format(name)
            return Response({'status': 'success', 'message': message})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        """Retrives an object based on id """

        return Response({'status': 'success', 'http_method': 'get'})

    def update(self, request, pk=None):
        """Updates an object based on id """

        return Response({'status': 'success', 'http_method': 'put'})

    def partial_update(self, request, pk=None):
        """Partially updates an objec. only few fields"""

        return Response({'status': 'success', 'http_method': 'patch'})

    def destroy(self, request, pk=None):
        """Deletes an object based on id"""

        return Response({'status': 'success', 'http_method': 'delete'})


class UserProfileViewSet(viewsets.ModelViewSet):
    """Handles CRUD operations on user profiles """

    serializer_class = UserProfileSerializer
    queryset = UserProfile.objects.all()

    authentication_classes = (TokenAuthentication,)
    permission_classes = (UpdateOwnProfile, IsAuthenticatedOrReadOnly)

    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'email')


class LoginViewSet(viewsets.ViewSet):
    """Checks email n password and returns auth Token """

    serializer_class = AuthTokenSerializer

    def create(self, request):
        """Use ObtainAuthToken APIView to validate and returns a Token """

        return ObtainAuthToken().post(request)


class ProfileFeedViewSet(viewsets.ModelViewSet):
    """Handles creating, reading and updating profile feed items."""


    serializer_class = ProfileFeedSerializer
    authentication_classes = (TokenAuthentication,)
    queryset = ProfileFeed.objects.all()

    permission_classes = (UpdateOwnProfileFeed, IsAuthenticatedOrReadOnly)

    def perform_create(self, serializer):
        """Sets the user profile to the logged in user."""

        serializer.save(user_profile=self.request.user)
