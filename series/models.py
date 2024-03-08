from django.db import models

from orgss.models import SubOrg
from assessment.models import AssessmentType
from sean.models import Item
from learningcourse.models import LearningCourse

class Series(models.Model):
    name = models.CharField(max_length=300)
    description = models.TextField(null=True, blank=True)
    thumbnail = models.FileField(upload_to="media/series/thumbnail", null=True, blank=True)
    sub_org = models.ForeignKey(SubOrg, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
    
class Seasons(models.Model):
    name = models.CharField(max_length=300)
    description = models.TextField(null=True, blank=True)
    thumbnail = models.FileField(upload_to="media/series/seasons/thumbnail", null=True, blank=True)
    series = models.ForeignKey(Series, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.name} - {self.series.name}"

class AssessmentSeason(models.Model):
    season = models.ForeignKey(Seasons, on_delete=models.CASCADE)
    assessment = models.ForeignKey(AssessmentType, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.season.name} - {self.assessment.name}"

class ItemSeason(models.Model):
    season = models.ForeignKey(Seasons, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.season.name} - {self.item.item_name}"

class LearningCourseSeason(models.Model):
    season = models.ForeignKey(Seasons, on_delete=models.CASCADE)
    learning_course = models.ForeignKey(LearningCourse, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.season.name} - {self.learning_course.name}"