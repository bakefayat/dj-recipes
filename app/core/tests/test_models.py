from django.test import TestCase
from django.contrib.auth import get_user_model
from core.models import Tags, Ingredients


def sample_user(email='bakefayat98@gmail.com', password='1234'):
    """create a sample user"""
    return get_user_model().objects.create_user(email, password)


class ModelTest(TestCase):

    def test_create_user_with_successful_email(self):
        email = 'mail@mail.com'
        password = '12345'

        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_user_with_normalized_email(self):
        email = 'mail@Mail.com'
        password = '12345'

        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email.lower())
        self.assertTrue(user.check_password(password))

    def test_user_with_invalid_email(self):
        '''Raise ValueError when email field is blank or None'''
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, '123')

    def test_create_superuser(self):
        email = 'eb@gmail.com'
        user = get_user_model().objects.create_superuser(
            email=email, password='1234'
            )
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)

    def test_tag_str(self):
        """Test the tag string representation"""
        tag = Tags.objects.create(
            user=sample_user(),
            name='vegan'
        )
        self.assertEqual(str(tag), tag.name)

    def test_ingredient_str(self):
        """Test the ingredient string representation"""
        ingredient = Ingredients.objects.create(
            user=sample_user(),
            name='cucumber'
        )
        self.assertEqual(str(ingredient), ingredient.name)
