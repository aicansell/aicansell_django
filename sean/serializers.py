from rest_framework import serializers

from sean.models import Item
from competency.serializers import CompetencySerializer, CompetencyListSerializer


class ItemLiSerializer(serializers.ModelSerializer):
    suborg = serializers.StringRelatedField()
    class Meta:
        model = Item
        fields = ['id','item_name', 'thumbnail', 'category', 'scenario_type', 'item_gender', 'role', 'item_type', 'level', 'suborg']

class ItemListSerializer1(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['id', 'item_emotion','coming_across_as']

class ItemCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['id', 'item_name', 'item_description', 'category', 'thumbnail', 'item_gender', 
                  'role', 'level', 'expert', 'competencys', 'is_live', 'is_approved']

class ItemSerializer(serializers.ModelSerializer):
    competencys = CompetencySerializer(many=True)

    class Meta:
        model = Item
        depth = 1
        fields = '__all__'   
        
class ItemUserSerializer(serializers.ModelSerializer):
    competencys = serializers.SerializerMethodField()
    role = serializers.SerializerMethodField()
    
    def get_competencys(self, obj):
        competencies = obj.competencys.all()
        return CompetencyListSerializer(competencies, many=True).data
    
    def get_role(self, obj):
        role = {
            'id': obj.role.id,
            'role_name': obj.role.name
        }
        return role
    
    class Meta:
        model = Item
        fields = ['id', 'item_name', 'item_answer', 'category', 'thumbnail', 'item_type', 'role',
                  'scenario_type', 'competencys', 'is_live', 'is_approved', 'level', 'expert']

class ItemEmotionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = [ 'item_answer', 'coming_across_as']
        
class ItemRecommendSerializer(serializers.ModelSerializer):
    competencys = CompetencySerializer(many=True)

    class Meta:
        model = Item
        depth = 1
        fields = ['coming_across_as','competencys']   
