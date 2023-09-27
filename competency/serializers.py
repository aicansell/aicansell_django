from rest_framework import serializers
from competency.models import Competency, Sub_Competency

class Sub_CompetencySerializer(serializers.ModelSerializer):
    class Meta:
        model = Sub_Competency
        fields = '__all__'
        
class CompetencySerializer(serializers.ModelSerializer):
    sub_compentency = serializers.SerializerMethodField()
    
    def get_sub_compentency(self, obj):
        sub_compentency = obj.sub_competency.all()
        return Sub_CompetencySerializer(sub_compentency, many=True).data
    
    class Meta:
        model = Competency
        fields = ['id', 'name', 'sub_compentency']
