from rest_framework import serializers

from assessment.models import Style, Situation
from assessment.models import Assessment1, Assessment2, Assessment3

class StyleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Style
        fields = ['id', 'name']
        
class SituationListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Situation
        fields = ['id', 'name']
    
class Assessment1Serializer(serializers.ModelSerializer):
    optionA = SituationListSerializer()
    optionB = SituationListSerializer()
    
    class Meta:
        model = Assessment1
        fields = ['optionA', 'optionB']

class Assessment2Serializer(serializers.ModelSerializer):
    optionA = SituationListSerializer()
    optionB = SituationListSerializer()
    
    class Meta:
        model = Assessment2
        fields = ['optionA', 'optionB']

class Assessment3Serializer(serializers.ModelSerializer):
    class Meta:
        model = Assessment3
        fields = ['id', 'choice']
