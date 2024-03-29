from django.db import models

from accounts.models import Account
from orgss.models import SubOrg

from datetime import date

class Question(models.Model):
    LEVEL = (
        ('easy', 'Easy'),
        ('hard', 'Hard'),
        ('difficult', 'Difficult'),
    )
    
    question = models.CharField(max_length=200)
    level = models.CharField(max_length=30, choices=LEVEL, default='easy')
    timer = models.IntegerField(null=True, blank=True)
    
    def __str__(self):
        return f"{self.question}-{self.level}"

class Option(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='options')
    option = models.CharField(max_length=200)
    is_correct = models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.question.question[:100]}-{self.option}-{self.is_correct}"

class AssessmentType(models.Model):
    TIGGER_POINT = (
        ('days', 'DAYS'),
        ('perentage', 'PERCENTAGE'),
    )
    
    name = models.CharField(max_length=100)
    suborg = models.ForeignKey(SubOrg, on_delete=models.CASCADE)
    passing_criteria = models.IntegerField(default=60)
    positive_marks = models.IntegerField(null=True, blank=True)
    negative_marks = models.IntegerField(null=True, blank=True)
    time = models.IntegerField(null=True, blank=True)
    trigger_point = models.CharField(max_length=30, choices=TIGGER_POINT, default=None)
    refresher_days = models.IntegerField(null=True, blank=True)
    
    def __str__(self):
        return f"{self.name}-{self.suborg.name}"

class Assessment(models.Model):
    ACCESS = (
        ('pre', 'PRE CHOICE'),
        ('mid', 'MID CHOICE'),
        ('post', 'POST CHOICE'),
    )
    
    assessment_type = models.ForeignKey(AssessmentType, on_delete=models.CASCADE)
    questions = models.ManyToManyField(Question)
    access = models.CharField(max_length=30, choices=ACCESS, default=None)
    is_approved = models.BooleanField(default=False)
    is_live = models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.assessment_type.name}-{self.access}"

class AssessmentResult(models.Model):
    ACCESS = (
        ('pre', 'PRE CHOICE'),
        ('mid', 'MID CHOICE'),
        ('post', 'POST CHOICE'),
    )
    
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    assessment = models.ForeignKey(Assessment, on_delete=models.CASCADE)
    phase = models.CharField(max_length=30, choices=ACCESS, default=None)
    result = models.IntegerField()
    created_at = models.DateField(default=date.today)
    
    def __str__(self):
        return f"{self.user.first_name}-{self.assessment.assessment_type.name}-{self.phase}-{self.result}"
