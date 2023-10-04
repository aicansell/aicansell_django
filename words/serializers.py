from rest_framework import serializers
from .models import Words, PowerWords, NegativeWords, EmotionWords

class WordSerializer(serializers.ModelSerializer):
    word_name = serializers.JSONField()
    class Meta:
        model = Words
        fields = '__all__'

class PowerWordsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PowerWords
        fields = "__all__"

class NegativeWordsSerializer(serializers.ModelSerializer):
    class Meta:
        model = NegativeWords
        fields = "__all__"
        
class EmotionWordsSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmotionWords
        fields = "__all__"        