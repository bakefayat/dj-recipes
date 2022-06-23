from django.urls import path
from .views import UsersCreateAPIView, CreateTokenView, ProfileRetriveUpdateAPIView

app_name = 'user'
urlpatterns = [
    path("create/", UsersCreateAPIView.as_view(), name="create"),
    path("token/", CreateTokenView.as_view(), name="token"),
    path("me/", ProfileRetriveUpdateAPIView.as_view(), name="me"),
]
