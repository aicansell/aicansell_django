from rest_framework import serializers

from assign.models import SeriesAssignUser
from series.serializers import SeriesListSerializer

class SeriesAssignUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = SeriesAssignUser
        fields = ["user", "series", "is_completed", "progress"]
        
class SeriesAssignUserListSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    series = serializers.SerializerMethodField()
    
    def get_user(self, obj):
        return obj.user.username
    
    def get_series(self, obj):
        return SeriesListSerializer(obj.series).data
    
    class Meta:
        model = SeriesAssignUser
        fields = ["id", "user", "series", "is_completed", "progress"]
