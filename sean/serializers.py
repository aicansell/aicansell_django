from rest_framework import serializers
from .models import Item 


class ItemListSerializer(serializers.ModelSerializer):
    item_role = serializers.StringRelatedField()
    class Meta:
        model = Item
        fields = ['id','item_name', 'item_description', 'thumbnail', 'category','tip', 'item_role']
