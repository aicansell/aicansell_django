from rest_framework import serializers
from .models import Words, PowerWords1, NegativeWords1, EmotionWords

class WordSerializer(serializers.ModelSerializer):
    word_name = serializers.JSONField()
    class Meta:
        model = Words
        fields = '__all__'

class PowerWordsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PowerWords1
        fields = "__all__"

class NegativeWordsSerializer(serializers.ModelSerializer):
    class Meta:
        model = NegativeWords1
        fields = "__all__"
        
class EmotionWordsSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmotionWords
        fields = "__all__"        