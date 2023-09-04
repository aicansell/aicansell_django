from rest_framework import serializers
from .models import Item 


class ItemListSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Item
        fields = ['id','item_name', 'item_description', 'thumbnail','tip']
