from rest_framework import serializers

from learningcourse.models import LearningCourse, LearningCourseVideo, LearningCourseDocument

class LearningCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = LearningCourse
        fields = ["name", "description", "thumbnail", "sub_org"]
        
class LearningCourseListSerializer(serializers.ModelSerializer):
    sub_org = serializers.SerializerMethodField()
    
    def get_sub_org(self, obj):
        return obj.sub_org.name
    
    class Meta:
        model = LearningCourse
        fields = ["id", "name", "description", "thumbnail", "sub_org"]
        
class LearningCourseVideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = LearningCourseVideo
        fields = ["course", "video"]
        
class LearningCourseVideoListSerializer(serializers.ModelSerializer):
    course = serializers.SerializerMethodField()
    
    def get_course(self, obj):
        return obj.course.name
    
    class Meta:
        model = LearningCourseVideo
        fields = ["id", "course", "video"]
        
class LearningCourseDocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = LearningCourseDocument
        fields = ["course", "document"]

class LearningCourseDocumentListSerializer(serializers.ModelSerializer):
    course = serializers.SerializerMethodField()
    
    def get_course(self, obj):
        return obj.course.name
    
    class Meta:
        model = LearningCourseDocument
        fields = ["id", "course", "document"]
