from rest_framework import serializers

from SnakeLadderGame.models import SnakeLadderGame, SnakeLadderGameResult
from SnakeLadderGame.models import Questions, Options

class SnakeLadderGameSerializer(serializers.ModelSerializer):
    class Meta:
        model = SnakeLadderGame
        fields = ['id', 'name', 'competency', 'description', 'thumbnail']
        
class SnakeLadderGameListSerializer(serializers.ModelSerializer):
    questions = serializers.SerializerMethodField()
    
    def get_questions(self, obj):
        data = Questions.objects.filter(snakeladdergame=obj)
        return QuestionsSerializer(data, many=True).data
    
    class Meta:
        model = SnakeLadderGame
        fields = ['id', 'name', 'competency', 'description', 'thumbnail', 'questions']
        
class QuestionsSerializer(serializers.ModelSerializer):
    options = serializers.SerializerMethodField()
    
    def get_options(self, obj):
        data = Options.objects.filter(question=obj)
        return OptionsSerializer(data, many=True).data
    
    class Meta:
        model = Questions
        fields = ['id', 'snakeladdergame', 'question', 'thumbnail', 'timer', 'options']
        
class OptionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Options
        fields = ['id', 'question', 'option', 'point']
        
class SnakeLadderGameResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = SnakeLadderGameResult
        fields = ['id', 'snakeladdergame', 'user', 'score', 'created_at']
