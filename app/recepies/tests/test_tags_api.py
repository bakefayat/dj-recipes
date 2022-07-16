from django.contrib.auth import get_user_model
from django.urls import reverse
from django.test import TestCase

from rest_framework import status
from rest_framework.test import APIClient

from core.models import Tags

from recepies.serializers import TagsSerializer

TAGS_URL = reverse('recepies:tags-list')


class PublicTagsApiTests(TestCase):
    """Tests tags api as public user"""
    def setUp(self):
        self.client = APIClient()
    
    def test_tag_list(self):
        """tests list of tags"""
        res = self.client.get(TAGS_URL)
        
        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)
    
class PrivateTagsApiTests(TestCase):
    """Test tags api as authorized user"""
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            'bakefayat98@gmail.com', 'password123'
        )
        self.client = APIClient()
        self.client.force_authenticate(self.user)
    
    def test_tag_list(self):
        """tests list of tags"""
        Tags.objects.create(user=self.user, name='vegan')
        Tags.objects.create(user=self.user, name='desert')
    
        res = self.client.get(TAGS_URL)
    
        tags = Tags.objects.all().order_by('-name')
        serialized_tags = TagsSerializer(tags, many=True)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(serialized_tags.data, res.data)

    def test_tags_limited_to_user(self):
        """test that shown tag belongs to authenticated user"""
        user2 = get_user_model().objects.create_user(
            'newone@new.com', 'pass123'
        )
        Tags.objects.create(user=user2, name='spice')
        tag = Tags.objects.create(user=self.user, name='comfort')
        res = self.client.get(TAGS_URL)
        
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(len(res.data), 1)
        self.assertEqual(res.data[0]['name'], tag.name)
