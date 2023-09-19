from rest_framework import serializers
from .models import Item


class ItemListSerializer(serializers.ModelSerializer):
    role = serializers.StringRelatedField()
    class Meta:
        model = Item
        fields = ['id','item_name', 'item_description', 'thumbnail', 'category', 'role', 'item_type', 'level']
        

class SeanSerializer(serializers.ModelSerializer):
    competency_power_word = serializers.StringRelatedField()

    class Meta:
        model = Item
        fields = ('competency_power_word', 'positive_traits') 

class ItemEmotionSerializer(serializers.ModelSerializer):
    #competency_power_word = serializers.StringRelatedField()
    competency_weak_word = serializers.StringRelatedField()
    

    class Meta:
        model = Item
        fields = [ 'item_answer' , 'competency_weak_word', 'coming_across_as', 'positive_traits', 'negative_traits']
        
    