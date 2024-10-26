from .models import Account, Order
from rest_framework import serializers


# Account Registration Serializer
class AccountRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=500, min_length=5, write_only=True)

    class Meta:
        model = Account
        fields = ['email', 'username', 'password']

    def create(self, validated_data):
        # Pop the password from validated_data
        password = validated_data.pop('password')

        # Create the user with the remaining validated_data
        account = Account(**validated_data)
        
        # Use set_password to hash the password before saving
        account.set_password(password)
        account.save()
        
        return account


# Order Serializer
class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'address', 'city', 'district', 'phone', 'email', 'note', 'address_op', 'company']

    def validate_phone(self, value):
        # Optional: Add custom phone validation logic
        if len(value) < 10:
            raise serializers.ValidationError("Phone number must be at least 10 digits long.")
        return value