from django.test import TestCase
from .models import Account

class AccountModelTest(TestCase):

    def setUp(self):
        self.user = Account.objects.create_user(
            email='testuser@example.com',
            username='testuser',
            
            password='password123'
        )

    def test_account_creation(self):
        """Test that a user is created correctly"""
        self.assertEqual(self.user.email, 'testuser@example.com')
        self.assertTrue(self.user.check_password('password123'))
        self.assertFalse(self.user.is_staff)  # Default value
        self.assertFalse(self.user.is_superuser)  # Default value
        self.assertTrue(self.user.is_active)  # Default value for is_active
        self.assertIsNotNone(self.user.created_at)  # Ensure created_at is auto-populated

    def test_create_user_without_email(self):
        """Test that creating a user without an email raises an error"""
        with self.assertRaises(ValueError):
            Account.objects.create_user(
                email=None,
                username='nouser',
                password='password123'
            )

    def test_create_superuser(self):
        """Test that a superuser is created with the correct fields"""
        superuser = Account.objects.create_superuser(
            email='superuser@example.com',
            username='superuser',
            password='superpassword123'
        )
        self.assertTrue(superuser.is_staff)
        self.assertTrue(superuser.is_superuser)
        self.assertTrue(superuser.is_active)
        self.assertEqual(superuser.email, 'superuser@example.com')
        self.assertTrue(superuser.check_password('superpassword123'))

    def test_username_uniqueness(self):
        """Test that the username must be unique"""
        with self.assertRaises(Exception):
            Account.objects.create_user(
                email='newuser@example.com',
                username='testuser',  # Same as the one in setUp
                password='password123'
            )