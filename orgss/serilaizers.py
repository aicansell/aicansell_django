from rest_framework import serializers

from industry.models import Industry

from industry.serializers import IndustrySerializer
from role.models import Role, Sub_Role
from competency.models import Sub_Competency
from role.serializers import RoleSerializer, SubRoleSerializer

from orgss.models import Org, Org_Roles, Weightage

from competency.serializers import CompetencySerializer


class OrgSerializer(serializers.ModelSerializer):
    industry_data = serializers.SerializerMethodField()
    
    def get_industry_data(self, obj):
        industry_data = Industry.objects.filter(id=obj.industry.id)
        return IndustrySerializer(industry_data, many=True).data
    
    class Meta:
        model = Org
        fields = ['id', 'name', 'description', 'industry', 'industry_data']


class OrgRolesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Org_Roles
        fields = ['id', 'org_role_name', 'org', 'org_role', 'org_subrole']
        
class OrgRolesListSerializer(serializers.ModelSerializer):
    org = serializers.SerializerMethodField()
    role = serializers.SerializerMethodField()
    subrole = serializers.SerializerMethodField()
    
    def get_org(self, obj):
        org = Org.objects.filter(id=obj.org.id)
        return OrgSerializer(org, many=True).data
    
    def get_role(self, obj):
        role = Role.objects.filter(id=obj.role.id)
        return RoleSerializer(role, many=True).data
    
    def get_subrole(self, obj):
        if obj.subrole:  # Check if subrole is not None
            subrole = Sub_Role.objects.filter(id=obj.subrole.id)
            return SubRoleSerializer(subrole, many=True).data
        return None  # Return None or an empty list depending on your requirements
    
    class Meta:
        model = Org_Roles
        fields = ['id', 'org_role_name', 'org', 'role', 'subrole']
     

class WeightageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Weightage
        fields = ['id', 'org_role', 'subcompetency', 'weightage']


class WeightageListSerializer(serializers.ModelSerializer):
    org_role = serializers.SerializerMethodField()
    competency = serializers.SerializerMethodField()
    
    def get_org_role(self, obj):
        org_role = Org_Roles.objects.filter(id=obj.org_role.id)
        return OrgRolesListSerializer(org_role, many=True).data
    
    def get_competency(self, obj):
        competency = Competency.objects.filter(id=obj.competency.id)
        return CompetencySerializer(competency, many=True).data
    
    class Meta:
        model = Weightage
        fields = ['id', 'org_role', 'competency', 'weightage']        