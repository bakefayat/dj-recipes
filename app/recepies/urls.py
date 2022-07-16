from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import TagsViewSet

router = DefaultRouter()
router.register('tags', TagsViewSet)

app_name = 'recepies'

urlpatterns = [
    path('', include(router.urls)),
]
