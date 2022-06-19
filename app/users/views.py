from .serializers import UserSerializer
from rest_framework import generics
# Create your views here.


class UsersCreateAPIView(generics.CreateAPIView):
    serializer_class = UserSerializer
    