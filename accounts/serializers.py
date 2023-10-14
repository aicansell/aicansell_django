from rest_framework import serializers
from .models import Account, Profile
from django.contrib.auth.models import User


class SignUpSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['email', 'first_name', 'last_name', 'password']

class UserSerializer(serializers.ModelSerializer):
    role = serializers.StringRelatedField()
    
    class Meta:
        model = Account
        fields = ['email', 'first_name', 'last_name', 'username', 'role', 'is_email_confirmed', 'user_role']

class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)

class ResetPasswordEmailSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)

class profileSerializer(serializers.ModelSerializer):
    class Meta:
        model=Profile
        fields="__all__"