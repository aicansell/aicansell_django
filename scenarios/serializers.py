from rest_framework import serializers

from scenarios.models import Scenarios
from words.serializers import PowerWordsSerializer, NegativeWordsSerializer

class ScenariosSerializer(serializers.ModelSerializer):
    power_words = serializers.SerializerMethodField()
    week_words = serializers.SerializerMethodField()
    
    def get_power_word(self, obj):
        power_word = obj.power_words.all()
        return PowerWordsSerializer(power_word, many=True).data
    
    def get_week_words(self, obj):
        week_word = obj.weak_words.all()
        return NegativeWordsSerializer(week_word, many=True).data
    
    class Meta:
        model = Scenarios
        fields = ('id', 'item_name', 'item_emotions', 'power_words', 'weak_words')
