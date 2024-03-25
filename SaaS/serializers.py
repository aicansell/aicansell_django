from rest_framework import serializers

from SaaS.models import Feature, FeatureList, SaaS

class FeatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feature
        fields = ['id', 'name', 'price', 'frequency', 'description']
        
class FeaturesListSerializer(serializers.ModelSerializer):
    featurelist = serializers.SerializerMethodField()
    
    def get_featurelist(self, obj):
        instances = FeatureList.objects.filter(feature=obj)
        return FeatureListSerializer(instances, many=True).data
    
    class Meta:
        model = Feature
        fields = ['id', 'name', 'price', 'frequency', 'description', 'featurelist']
        
class FeatureListSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeatureList
        fields = ['id', 'name', 'frequency', 'times']
        
class SaaSSerializer(serializers.ModelSerializer):
    class Meta:
        model = SaaS
        fields = ['id', 'user', 'feature', 'startdate', 'enddate']
        
class SaaSListSerializer(serializers.ModelSerializer):
    feature = serializers.SerializerMethodField()
    
    def get_feature(self, obj):
        return FeaturesListSerializer(obj.feature).data
    
    class Meta:
        model = SaaS
        fields = ['id', 'user', 'feature', 'startdate', 'enddate']
