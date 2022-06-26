from django.contrib.auth import get_user_model
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework import generics, authentication, permissions
from .serializers import UserSerializer, AuthTokenSerializer
from .permissions import IsSuperUser


class UsersCreateAPIView(generics.CreateAPIView):
    serializer_class = UserSerializer


class CreateTokenView(ObtainAuthToken):
    """Create a new auth token for user"""
    serializer_class = AuthTokenSerializer
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


class ProfileRetriveUpdateAPIView(generics.RetrieveUpdateAPIView):
    """retrive and update profile"""
    serializer_class = UserSerializer
    authentication_classes = (authentication.TokenAuthentication, )
    permission_classes = (permissions.IsAuthenticated, )

    def get_object(self):
        return self.request.user


class UsersListAPIView(generics.ListAPIView):
    """list of users"""
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
    authentication_classes = (authentication.TokenAuthentication, )
    permission_classes = (IsSuperUser, )
