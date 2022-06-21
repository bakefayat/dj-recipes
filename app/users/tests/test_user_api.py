from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

from rest_framework.test import APIClient
from rest_framework import status


CREATE_USER_URL = reverse('users:create')
CREATE_TOKEN_URL = reverse('users:token')

def create_user(**params):
    return get_user_model().objects.create_user(**params)

class PublicUserApiTests(TestCase):
    """Test the users API (public)"""

    def setUp(self):
        self.client = APIClient()

    def test_create_valid_user_success(self):
        """Test creating user with valid params"""
        payload = {
            'email': 'test@ehsan.com',
            'password': 'testpass',
            'name': 'Test name'
        }
        res = self.client.post(CREATE_USER_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        user = get_user_model().objects.get(**res.data)
        self.assertEqual(user.password, payload['password'])
        self.assertNotIn('password', res.data)



    def test_user_exists(self):
        """ Test creating user that already exists fails"""
        payload = {
            'email':  'test@eb.com',
            'password': 'validpassword',
            'name': 'ehsan bakefayat'
        }
        create_user(**payload)
        
        res = self.client.post(CREATE_USER_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
    
    def test_password_too_short(self):
        payload = {
            'email': 'test@eb.com',
            'password': '12',
            'name': 'ehsan bakefayat'
        }

        res = self.client.post(CREATE_USER_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
        user_exists = get_user_model().objects.filter(
            email = payload['email']
        ).exists()
        self.assertFalse(user_exists)

    def test_create_token_for_user(self):
        """Test that token is created for the user"""
        payload = {
            'email': 'bakefayat@test.com',
            'password': 'testpass'
        }
        create_user(**payload)
        res = self.client.post(CREATE_TOKEN_URL, payload)

        self.assertIn('token', res.data)
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_create_token_invalid_credentials(self):
        """Test that token is not created for user with invalid credentials"""
        create_user(email="bakefayat@test.com", password="okaypassword")
        payload = {
            'username': 'bakefayat@test.com',
            'password': 'wrongpassword',
        }
        res = self.client.post(CREATE_TOKEN_URL, payload)

        self.assertNotIn('token', res.data)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
    
    def test_create_token_unregistered_user(self):
        """Test that token is not created for user that isnt registered"""
        payload = {
            'username': 'bakefayat@test.com',
            'password': 'okaypassword'
        }
        res = self.client.post(CREATE_TOKEN_URL, payload)

        self.assertNotIn('token', res.data)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_token_missing_field(self):
        """Test that email and password are required"""
        payload = {
            'username': 'bakefayat@test.com',
            'passowrd': ''
        }
        res = self.client.post(CREATE_TOKEN_URL, payload)

        self.assertNotIn('token', res.data)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
