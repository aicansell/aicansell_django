from rest_framework import serializers
from accounts.models import Account, Profile
from django.contrib.auth.models import User

class LoginSerializer(serializers.ModelSerializer):
    role = serializers.SerializerMethodField()
    org = serializers.SerializerMethodField()
    
    def get_role(self, obj):
        return getattr(obj.role, 'name', None)
    
    def get_org(self, obj):
        org_name = getattr(obj.org, 'name', None)
        org_logo = None
        if hasattr(obj.org, 'logo') and obj.org.logo:
            org_logo = obj.org.logo.url
        return {'name': org_name, 'logo': org_logo}
    
    class Meta:
        model = Account
        exclude = (
            'password', 'last_login', 'is_active', 'is_staff', 'date_joined',
            'is_admin', 'is_superadmin', 
        )

class SignUpSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['email', 'first_name', 'last_name', 'password', 'org', 'username']

class UserSerializer(serializers.ModelSerializer):
    role = serializers.StringRelatedField()
    
    class Meta:
        model = Account
        fields = ['id', 'email', 'first_name', 'last_name', 'username', 'role', 'is_email_confirmed', 'user_role']

class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)

class ResetPasswordEmailSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)

class profileSerializer(serializers.ModelSerializer):
    class Meta:
        model=Profile
        fields="__all__"