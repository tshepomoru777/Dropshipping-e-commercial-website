from django.test import TestCase
from .models import Account

class AccountModelTest(TestCase):
    def setUp(self):
        self.user = Account.objects.create_user(
            email='testuser@example.com',
            username='testuser',
            salt='somesalt',
            password='password123'
        )

    def test_account_creation(self):
        """Test that a user is created correctly"""
        self.assertEqual(self.user.email, 'testuser@example.com')
        self.assertTrue(self.user.check_password('password123'))
        self.assertFalse(self.user.is_staff)  # Default value
        self.assertFalse(self.user.is_superuser)  # Default value
