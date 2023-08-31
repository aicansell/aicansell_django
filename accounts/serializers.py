from rest_framework import serializers
from .models import Account
from django.contrib.auth.models import User


class SignUpSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['email', 'first_name', 'last_name', 'password']

class UserSerializer(serializers.ModelSerializer):
    user_role = serializers.StringRelatedField()
    user_subrole = serializers.StringRelatedField()
    user_org = serializers.StringRelatedField()
    class Meta:
        model = Account
        fields = ['email', 'first_name', 'last_name', 'username', 'password','user_org','user_role', 'user_subrole']



