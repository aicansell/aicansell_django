from rest_framework import serializers
from sean.models import Item


class ItemListSerializer(serializers.ModelSerializer):
    role = serializers.StringRelatedField()
    user = serializers.SerializerMethodField()
    
    def get_user(self, obj):
        if obj.user:
            return obj.user.first_name
        return None

    class Meta:
        model = Item
        fields = ['id', 'item_name', 'item_description', 'thumbnail', 'category', 'role', 'item_type', 'level', 'user']

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'
        

class SeanSerializer(serializers.ModelSerializer):
    competency_power_word = serializers.StringRelatedField()

    class Meta:
        model = Item
        fields = ('competency_power_word', 'positive_traits') 



class ItemRecommendSerializer(serializers.ModelSerializer):
    competency_weak_words = serializers.StringRelatedField(many=True)
    competency_power_words = serializers.StringRelatedField(many=True)

    class Meta:
        model = Item
        fields = ['positive_traits', 'competency_weak_words', 'competency_power_words']
    


class ItemEmotionSerializer(serializers.ModelSerializer):
    
    #competency_weak_words = serializers.StringRelatedField(many=True)
    #competency_power_words = serializers.StringRelatedField(many=True)
    

    class Meta:
        model = Item
        fields = [ 'item_answer', 'coming_across_as', 'positive_traits', 'negative_traits']
        
    