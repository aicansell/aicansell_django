from django.contrib.auth.password_validation import validate_password

from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from accounts.models import Account

class UsersListSerializer(serializers.ModelSerializer):
    role = serializers.SerializerMethodField()
    org = serializers.SerializerMethodField()
    
    def get_role(self, obj):
        return getattr(obj.role, 'name', None)
    
    def get_org(self, obj):
        return getattr(obj.org, 'name', None)
    
    class Meta:
        model = Account
        fields = ['id', 'first_name', 'last_name', 'email', 'username', 'user_role', 'is_email_confirmed', 'role', 'org', 'active']

class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['id', 'first_name', 'last_name', 'email', 'username', 'user_role', 'is_email_confirmed', 'role', 'org', 'active']

class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['first_name', 'last_name', 'email', 'username', 'user_role', 'role', 'org', 'active']
        extra_kwargs = {
            'email': {'required': True, 'validators': [UniqueValidator(queryset=Account.objects.all())]},
        }

    def create(self, validated_data):
        user_role = validated_data.get('user_role', 'user')
        user = Account.objects.create(
            username = validated_data.get('username'),
            email = validated_data['email'],
            first_name = validated_data.get('first_name'),
            last_name = validated_data.get('last_name'),
            user_role = user_role,
            role = validated_data.get('role'),
            org = validated_data.get('org'),
            active = True,
        )
        
        user.set_password("aicansell@123")
        user.save()
        return user
