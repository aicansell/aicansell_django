from rest_framework import serializers
from .models import Sub_Competency

class Sub_CompetencySerializer(serializers.ModelSerializer):
    subcompetency_name = serializers.JSONField()
    class Meta:
        model = Sub_Competency
        fields = '__all__'