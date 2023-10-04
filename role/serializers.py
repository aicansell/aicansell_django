from rest_framework import serializers

from role.models import Role, Sub_Role

class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = ['id', 'name']
        
class SubRoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sub_Role
        fields = ['id', 'role', 'subrole']