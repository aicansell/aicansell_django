from django.contrib.auth.password_validation import validate_password

from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from accounts.models import Account
from users.models import UserSubOrgs, UserMapping
from users.models import UserRights, UserRightsMapping
from constants import DEFAULT_PASSWORD

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
        
        user.set_password(DEFAULT_PASSWORD)
        user.save()
        return user

class UserSubOrgSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserSubOrgs
        fields = ['id', 'user', 'suborg']

class UserSubOrgListSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    sub_org = serializers.SerializerMethodField()
    
    def get_user(self, obj):
        return getattr(obj.user, 'username', None)
    
    def get_sub_org(self, obj):
        return getattr(obj.sub_org, 'name', None)
    
    class Meta:
        model = UserSubOrgs
        fields = ['id', 'user', 'suborg']

class UserMappingSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserMapping
        fields = ['id', 'user', 'admin']

class UserMappingListSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    admin = serializers.SerializerMethodField()
    
    def get_user(self, obj):
        return getattr(obj.user, 'username', None)
    
    def get_admin(self, obj):
        return getattr(obj.admin, 'username', None)
    
    class Meta:
        model = UserMapping
        fields = ['id', 'user', 'admin']

class UserRightSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserRights
        fields = ['id', 'name']

class UserRightsMappingSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserRightsMapping
        fields = ['id', 'user', 'right']

class UserRightsMappingSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserRightsMapping
        fields = ['id', 'user', 'right']

class UserRightsMappingListSerializer(serializers.ModelSerializer):
    right = serializers.SerializerMethodField()
    
    def get_right(self, obj):
        return getattr(obj.right, 'name', None)
    
    class Meta:
        model = UserRightsMapping
        fields = ['id', 'right']
