from rest_framework import serializers

from series.models import Series, Seasons

class SeriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Series
        fields = ["name", "description", "thumbnail", "sub_org"]
        
class SeriesListSerializer(serializers.ModelSerializer):
    sub_org = serializers.SerializerMethodField()
    
    def get_sub_org(self, obj):
        return obj.sub_org.name
    
    class Meta:
        model = Series
        fields = ["id", "name", "description", "thumbnail", "sub_org"]

class SeasonsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seasons
        fields = ["name", "description", "thumbnail", "series"]
        
class SeasonsListSerializer(serializers.ModelSerializer):
    series = serializers.SerializerMethodField()
    
    def get_series(self, obj):
        return obj.series.name
    
    class Meta:
        model = Seasons
        fields = ["id", "name", "description", "thumbnail", "series"]
