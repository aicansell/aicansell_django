from rest_framework import serializers

from accounts.models import Account
from orgss.models import Org_Roles
from orgss.serilaizers import OrgRolesSerializer

class UsersListSerializer(serializers.ModelSerializer):
    role = serializers.SerializerMethodField()
    
    def get_role(self, obj):
        return OrgRolesSerializer(obj.role).data
    
    class Meta:
        model = Account
        fields = ['id', 'first_name', 'last_name', 'email', 'username', 'user_role', 'is_email_confirmed', 'role']

class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['id', 'first_name', 'last_name', 'email', 'username', 'user_role', 'is_email_confirmed', 'role']
