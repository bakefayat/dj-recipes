from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import TagsViewSet, IngredientsViewSet

router = DefaultRouter()
router.register('tags', TagsViewSet)
router.register('ingredients', IngredientsViewSet)

app_name = 'recepies'

urlpatterns = [
    path('', include(router.urls)),
]
