from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet, ModelViewSet

from profiles_api import permissions
from .models import UserProfile

from .serializers import HelloSerializer, UserSerializers


# Create your views here.



class HelloApiView(APIView):
    """ TEST API VIEW """

    serializer_class = HelloSerializer

    def get(self, request, format=None):
        api_view = ['XXXX', 'Hi']
        return Response(data={"Me": "Bad Boy", "api_view": api_view})

    def post(self, request):
        """  Creates a hello msg with our name  """
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'name is  : {name}'
            return Response({"message", message})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        """ Handles updating of an object """
        return Response({"method": "put"})

    def patch(self, request, pk=None):
        """ Handles updating of an object partially """
        return Response({"method": "patch"})

    def delete(self, request, pk=None):
        """ Handles deleting of an object """
        return Response({"method": "delete"})


class HelloViewSet(ViewSet):
    serializer_class = HelloSerializer

    def list(self, request):
        """ Returns a  list """
        items = [1, 2, 3, 4]
        return Response({"message": "Hello", "A ViewSet": items})

    def create(self, request):
        """ creating new objects """
        """  Creates a hello msg with our name  """
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'name is  : {name}'
            return Response({"message", message})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        """ getting a specific object by id """
        return Response({"http_method": "get"})

    def update(self, request, pk=None):
        """ updating an object """
        return Response({"http_method": "put"})

    def partial_update(self, request, pk=None):
        """ updating a  part of an object """
        return Response({"http_method": "patch"})

    def destroy(self, request, pk=None):
        """  destroy an object  """
        return Response({"http_method": "delete"})


""" Handles creating & updating of Profiles """


class UserProfileViewSet(ModelViewSet):
    serializer_class = UserSerializers
    # queryset attribute must be required is we are not mentioning base_name is urls.py while registering this ViewSet
    queryset = UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile, )
