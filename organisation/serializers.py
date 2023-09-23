from rest_framework import serializers

from organisation.models import Org, Org_Roles, Weightage


class OrgSerializer(serializers.ModelSerializer):
    class Meta:
        model = Org
        fields = ['id', 'name', 'description', 'industry']


class OrgRolesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Org_Roles
        fields = ['id', 'org_role_name', 'org', 'org_role', 'org_subrole']


class Weightage(serializers.ModelSerializer):
    class Meta:
        model = Weightage
        fields = ['id', 'org_role', 'subcompetency', 'weight']
