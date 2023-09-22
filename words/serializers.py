from rest_framework import serializers
from .models import Words

class WordSerializer(serializers.ModelSerializer):
    word_name = serializers.JSONField()
    class Meta:
        model = Words
        fields = '__all__'