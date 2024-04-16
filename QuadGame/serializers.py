from rest_framework import serializers

from QuadGame.models import QuadGame, Quadrant, QuadGameResult
from QuadGame.models import Statements, Questions

class QuadGameSerializer(serializers.ModelSerializer):
    quadrants = serializers.SerializerMethodField()
    questions = serializers.SerializerMethodField()
    
    def get_quadrants(self, obj):
        instances = Quadrant.objects.filter(quadgame=obj)
        return QuadrantSerializer(instances, many=True).data
    
    def get_questions(self, obj):
        instances = Questions.objects.filter(quadgame=obj)
        return QuestionsSerializer(instances, many=True).data
    
    class Meta:
        model = QuadGame
        fields = ['id', 'name', 'thubmnail', 'description', 'competency', 
                  'postive_marks', 'negative_marks', 'quadrants', 'questions']
        
class QuadrantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quadrant
        fields = ['id', 'name', 'thubmnail', 'quadgame']
        
class StatementsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Statements
        fields = ['id', 'statement', 'thumbnail', 'quadrant']
        
class QuestionsSerializer(serializers.ModelSerializer):
    statements = serializers.SerializerMethodField()
    
    def get_statements(self, obj):
        return StatementsSerializer(obj.statements, many=True).data
    
    class Meta:
        model = Questions
        fields = ['id', 'question', 'thumbnail', 'quadgame', 'statements', 'timer']
        
class QuadGameResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuadGameResult
        fields = ['id', 'quadgame', 'user', 'score', 'created_at']
