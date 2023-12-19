from rest_framework import serializers
from .models import Quiz


class QuizListSerializer(serializers.ModelSerializer):
    option1 = serializers.StringRelatedField()
    option2 = serializers.StringRelatedField()
    option3 = serializers.StringRelatedField()
    class Meta:
        model = Quiz
        fields = ['id','item_name', 'option1', 'option2', 'option3', 'QuizAnswer_CHOICES']
        



class QuizResultSerializer(serializers.ModelSerializer):
    feedback1 = serializers.StringRelatedField()
    feedback2 = serializers.StringRelatedField()
    feedback3 = serializers.StringRelatedField()
    class Meta:
        model = Quiz
        fields = ['id','feedback1', 'feedback2', 'feedback3']
     

