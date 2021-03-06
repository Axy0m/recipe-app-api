from django.test import TestCase
from django.contrib.auth import get_user_model
from core import models



def sample_user(email='test@londonappdev.com', password='testpass'):

    """Create a sample user"""

    return get_user_model().objects.create_user(email, password)


class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        
        """TEST CREATING A NEW USER WITH AN EMAIL IS SUCCESSFUL"""


        email = 'sjfaedxqeejftde@scpulse.com'
        password = 'Testpass123'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))


    def test_new_user_email_normalized(self):
        
        """TEST THE EMAIL FOR A NEW USER IS NORMALIZED"""


        email = 'sjfaedxqeejftde@scpulse.com'
        user = get_user_model().objects.create_user(email, 'test123')

        self.assertEqual(user.email, email.lower())


    def test_new_user_invalid_email(self):

        """TEST CREATING USER WITH NO EMAIL RAISES ERROR"""

        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'test123')

    def test_create_new_superuser(self):

        """TEST CREATING A NEW SUPERUSER"""

        user = get_user_model().objects.create_superuser(
            'sjfaedxqeejftde@scpulse.com',
            'test123'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)



    def test_tag_str(self):

        """Test the tag string representation"""
        
        tag = models.Tag.objects.create(
            user=sample_user(),
            name='Vegan'
        )

        self.assertEqual(str(tag), tag.name)


    def test_ingredient_str(self):

        """Test the ingredient string representation"""
        
        ingredient = models.Ingredient.objects.create(
            user=sample_user(),
            name='Cucumber'
        )

        self.assertEqual(str(ingredient), ingredient.name)