from rest_framework import serializers
from .models import Item
#from competency.models import Competency1
from competency.serializers import CompetencySerializer

"""
class ItemListSerializer(serializers.ModelSerializer):
    role = serializers.StringRelatedField()
    #competency_power_words = serializers.StringRelatedField(many=True)
    #competencys = serializers.StringRelatedField(many=True)
    class Meta:
        model = Item
        fields = ['id','item_name', 'item_description', 'thumbnail', 'category', 'role', 'item_type', 'level']
        #fields = ['id','item_name', 'competencys', 'thumbnail', 'category', 'role', 'item_type', 'competency_power_words']
"""

class ItemListSerializer1(serializers.ModelSerializer):
    role = serializers.StringRelatedField()

    class Meta:
        model = Item
        fields = ['id', 'item_name', 'item_emotion', 'thumbnail', 'category', 'role', 'item_type', 'scenario_type','level', 'user_powerwords', 'user_weakwords']     

class ItemSerializer(serializers.ModelSerializer):
    role = serializers.StringRelatedField()
    #competencys = CompetencySerializer(many=True)

    class Meta:
        model = Item
        #depth = 1
        #fields = '__all__'
        fields = ['id', 'item_name', 'item_emotion', 'thumbnail', 'category', 'role', 'scenario_type', 'item_type', 
                    'item_answercount', 'item_gender', 'level', 'coming_across_as', 'get_competencys_as_string',
                    'user_powerwords', 'user_weakwords']

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