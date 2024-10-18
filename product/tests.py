from rest_framework.test import APITestCase
from rest_framework import status
from .serializers import AccountRegisterSerializer

class AccountSerializerTest(APITestCase):
    def test_account_serializer(self):
        data = {
            'email': 'newuser@example.com',
            'username': 'newuser',
            'password': 'newpassword123',
            'salt': 'randomsalt'
        }
        serializer = AccountRegisterSerializer(data=data)
        self.assertTrue(serializer.is_valid())
        self.assertEqual(serializer.validated_data['email'], 'newuser@example.com')
