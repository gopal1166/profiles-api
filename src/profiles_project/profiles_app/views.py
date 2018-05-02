from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import HttpResponse
from . import serializers

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
