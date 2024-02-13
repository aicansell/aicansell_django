from django.db import models

from accounts.models import Account

class Style(models.Model):
    name = models.CharField(max_length=100)
    msg = models.TextField(null=True, blank=True)
    
    def __str__(self):
        return self.name
    
class Situation(models.Model):
    name = models.CharField(max_length=500)
    style = models.ForeignKey(Style, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
    
class Assessment1(models.Model):
    ACCESS = (
        ('pre', 'PRE CHOICE'),
        ('mid', 'MID CHOICE'),
        ('post', 'POST CHOICE'),
    )
    
    optionA = models.ForeignKey(Situation, on_delete=models.CASCADE, related_name='optionA')
    optionB = models.ForeignKey(Situation, on_delete=models.CASCADE, related_name='optionB')
    access = models.CharField(max_length=20, choices=ACCESS, default=None)
    
    def __str__(self):
        return f'{self.optionA.name} {self.optionB.name}'

class Assessment2(models.Model):
    ACCESS = (
        ('pre', 'PRE CHOICE'),
        ('mid', 'MID CHOICE'),
        ('post', 'POST CHOICE'),
    )
    
    optionA = models.ForeignKey(Situation, on_delete=models.CASCADE, related_name='optionA2')
    optionB = models.ForeignKey(Situation, on_delete=models.CASCADE, related_name='optionB2')
    access = models.CharField(max_length=20, choices=ACCESS, default=None)
    
    def __str__(self):
        return f'{self.optionA.name} {self.optionB.name}'

class Assessment3(models.Model):
    ACCESS = (
        ('pre', 'PRE CHOICE'),
        ('mid', 'MID CHOICE'),
        ('post', 'POST CHOICE'),
    )
    
    choice = models.CharField(max_length=500)
    access = models.CharField(max_length=20, choices=ACCESS, default=None)
    
    def __str__(self):
        return self.choice[:200]

class Assessment(models.Model):
    name = models.CharField(max_length=100)
    
class AssessmentResult(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    assessment = models.ForeignKey(Assessment, on_delete=models.CASCADE)
    phase = models.CharField(max_length=20, choices=[('pre', 'PRE CHOICE'), ('mid', 'MID CHOICE'), ('post', 'POST CHOICE')])
    result = models.CharField(max_length=100, default="")

    def __str__(self):
        return f"{self.user.username} - {self.assessment.name} - {self.phase}"
