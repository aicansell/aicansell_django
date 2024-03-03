from rest_framework import serializers

from assessment.models import Question, Option, AssessmentType
from assessment.models import Assessment, AssessmentResult

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ['id', 'question', 'level', 'timer']
        
class OptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Option
        fields = ['id', 'question', 'option', 'is_correct']
        
class OptionListSerializer(serializers.ModelSerializer):
    question = serializers.SerializerMethodField()
    
    def get_question(self, obj):
        return obj.question.question
    
    class Meta:
        model = Option
        fields = ['id', 'question', 'option', 'is_correct']
    
class AssessmentTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = AssessmentType
        fields = ['id', 'name', 'suborg', 'passing_criteria', 'positive_marks', 'negative_marks', 'time', 'trigger_point', 'refresher_days']

class AssessmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assessment
        fields = ['id', 'assessment_type', 'questions', 'access']

class AssessmentResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = AssessmentResult
        fields = ['id', 'user', 'assessment', 'phase', 'result']
