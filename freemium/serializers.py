from rest_framework import serializers
from .models import Freemium

class FreemiumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Freemium
        fields = '__all__'