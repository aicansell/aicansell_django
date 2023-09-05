from rest_framework import serializers
from .models import Account
from django.contrib.auth.models import User


class SignUpSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['email', 'first_name', 'last_name', 'password']

class UserSerializer(serializers.ModelSerializer):
    userorg_roles = serializers.StringRelatedField()
    
    class Meta:
        model = Account
        fields = ['email', 'first_name', 'last_name', 'username', 'password','userorg_roles']

class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)

class ResetPasswordEmailSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)

