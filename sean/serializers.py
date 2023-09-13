from rest_framework import serializers
from .models import Item 


class ItemListSerializer(serializers.ModelSerializer):
    role = serializers.StringRelatedField()
    class Meta:
        model = Item
        fields = ['id','item_name', 'item_description', 'thumbnail', 'category', 'role']
        

class ItemEmotionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Item
        fields = [ 'item_answer', 'competency_power_word', 'competency_weak_word', 'coming_across_as']