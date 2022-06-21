from django.urls import path
from .views import UsersCreateAPIView, CreateTokenView

app_name = "users"
urlpatterns = [
    path("create/", UsersCreateAPIView.as_view(), name="create"),
    path("api/", CreateTokenView.as_view(), name="token")
]
