from rest_framework import serializers

from freemium.models import Freemium, Subscription

class FreemiumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Freemium
        fields = ['id', 'name', 'description', 'amount', 'duration', 'access']
        
class SubscriptionSerializer(serializers.ModelSerializer):
    service = serializers.SerializerMethodField()
    
    def get_service(self, obj):
        return FreemiumSerializer(obj.service).data
    
    class Meta:
        model = Subscription
        fields = ['id', 'user', 'service', 'start_date_time', 'end_date_time', 'is_expired']
