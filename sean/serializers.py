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

class ItemSerializer(serializers.ModelSerializer):
    competencys = CompetencySerializer(many=True)

    class Meta:
        model = Item
        depth = 1
        fields = '__all__'   
        
class ItemUserSerializer(serializers.ModelSerializer):
    competencys = serializers.SerializerMethodField()
    
    def get_competencys(self, obj):
        competencies = obj.competencys.all()
        return CompetencyListSerializer(competencies, many=True).data
    
    class Meta:
        model = Item
        fields = ['id', 'item_name', 'item_answer', 'category', 'thumbnail', 'item_type', 'scenario_type', 'competencys',]

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
