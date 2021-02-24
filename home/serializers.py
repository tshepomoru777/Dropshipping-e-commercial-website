from .models import Account, Token
from rest_framework import serializers



class AccountRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=500, min_length=5, write_only=True)

    class Meta:
        model = Account
        fields = ['email', 'username', 'password', 'salt']

    def validate(self, attrs):
        email = attrs.get('email', '')
        username = attrs.get('username', '')

        if not username.isalnum():
            raise serializers.ValidationError('Username should only contain alphanumeric character')
        return attrs


class AccountLoginSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField()

class TokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Token
        fields = ['user_id', 'token']