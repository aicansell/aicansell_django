from rest_framework import serializers

from scenarios.models import Scenarios
from words.serializers import PowerWordScenariosSerializer, NegativeWordScenarioSerializer

class ScenariosSerializer(serializers.ModelSerializer):
    power_words = serializers.SerializerMethodField()
    negative_words = serializers.SerializerMethodField()
    
    def get_power_words(self, obj):
        power_word = obj.power_words.all()
        return PowerWordScenariosSerializer(power_word, many=True).data
    
    def get_negative_words(self, obj):
        negative_word = obj.negative_words.all()
        return NegativeWordScenarioSerializer(negative_word, many=True).data
    
    class Meta:
        model = Scenarios
        fields = ['id', 'item_name', 'item_emotions', 'power_words', 'negative_words']

class ScenariosCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Scenarios
        fields = ['id', 'item_name', 'item_emotions', 'power_words', 'negative_words']
