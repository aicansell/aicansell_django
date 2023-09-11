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
        fields = [ 'item_answer', 'power_words', 'weak_words', 'coming_across_as']