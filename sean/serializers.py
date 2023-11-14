from rest_framework import serializers
from .models import Item
#from competency.models import Competency1
from competency.serializers import CompetencySerializer, CompetencyListSerializer
from competency.models import Competency


class ItemLiSerializer(serializers.ModelSerializer):
    role = serializers.StringRelatedField()
    #competency_power_words = serializers.StringRelatedField(many=True)
    #competencys = serializers.StringRelatedField(many=True)
    class Meta:
        model = Item
        fields = ['id','item_name', 'thumbnail', 'category', 'scenario_type', 'item_gender', 'role', 'item_type', 'level']
        #fields = ['id','item_name', 'competencys', 'thumbnail', 'category', 'role', 'item_type', 'competency_power_words']


class ItemListSerializer1(serializers.ModelSerializer):
    #role = serializers.StringRelatedField()
    #competencys = CompetencySerializer(many=True)

    class Meta:
        model = Item
        #depth = 1
        #fields = '__all__'
        fields = ['id', 'item_emotion','user_powerwords', 'user_weakwords', 'coming_across_as']

    """
    def create(self, validated_data):
        competencys_data = validated_data.pop('competencys', [])  # Remove books from validated data
        item = Item.objects.create(**validated_data)

        # Associate book instances with the author
        item.competencys.set(competencys_data)

        return item   """ 

class ItemSerializer(serializers.ModelSerializer):
    #role = serializers.StringRelatedField()
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
    
    #competency_weak_words = serializers.StringRelatedField(many=True)
    #competency_power_words = serializers.StringRelatedField(many=True)
    

    class Meta:
        model = Item
        fields = [ 'item_answer', 'coming_across_as', 'positive_traits', 'negative_traits']
        
class ItemRecommendSerializer(serializers.ModelSerializer):
    
    competencys = CompetencySerializer(many=True)

    class Meta:
        model = Item
        depth = 1
        fields = ['coming_across_as','competencys']   
