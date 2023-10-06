from rest_framework import serializers

from industry.models import Industry

class IndustrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Industry
        fields = ['id', 'industry_name', 'industry_description']