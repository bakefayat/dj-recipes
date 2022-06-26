from django.urls import path
from .views import (
                    UsersCreateAPIView, CreateTokenView,
                    ProfileRetriveUpdateAPIView, UsersListAPIView
                    )

app_name = "users"
urlpatterns = [
    path("create/", UsersCreateAPIView.as_view(), name="create"),
    path("token/", CreateTokenView.as_view(), name="token"),
    path("profile/", ProfileRetriveUpdateAPIView.as_view(), name="profile"),
    path("list/", UsersListAPIView.as_view(), name="list"),
]
