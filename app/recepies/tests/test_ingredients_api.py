from http.client import InvalidURL
from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from rest_framework.test import APIClient
from rest_framework import status

from core.models import Ingredients

from recepies.serializers import IngredientsSerializer


INGREDIENTS_URL = reverse("recepies:ingredients-list")


class PublicIngredientsApiTests(TestCase):
    """Test ingredients API as public user"""

    def setUp(self):
        self.client = APIClient()

    def test_login_required(self):
        """Test that Ingredients API are not allowed as public"""
        res = self.client.get(INGREDIENTS_URL)

        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)
    
class PrivateIngredientsApiTests(TestCase):
    """Test ingredients Api as private user"""
    def setUp(self):
        self.client = APIClient()
        self.user = get_user_model().objects.create(
            "bakefayat@gmail.com",
            "password123"
        )
        self.client.force_authenticate(self.user)
    
    def test_retrive_list_endpoint(self):
        """Test retriving list of ingredients"""
        Ingredients.objects.create(name='kale', user=self.user)
        Ingredients.objects.create(name='salt', user=self.user)
        
        ingredients = Ingredients.objects.all().order_by('-name')
        serializer = IngredientsSerializer(ingredients, many=True)

        res = self.client.get(INGREDIENTS_URL)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serializer.data)

    def test_ingredients_limited_to_user(self):
        """Test that returned ingredients belonged to authenticated user"""
        user2 = get_user_model().objects.create(
            'james',
            'pass123')
        Ingredients.objects.create(name='celery', user=user2)
        ingredient = Ingredients.objects.create(name='salt', user=self.user)

        res = self.client.get(INGREDIENTS_URL)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(len(res.data), 1)
        self.assertEqual(res.data[0]['name'], ingredient.name)
