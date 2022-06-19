from django.urls import path
from .views import UsersCreateAPIView

app_name = "users"
urlpatterns = [
    path("create/", UsersCreateAPIView.as_view(), name="create"),
]