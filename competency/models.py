from django.db import models

from words.models import PowerWords1, NegativeWords1, EmotionWords


# Create your models here.

class Sub_Competency(models.Model):
    def __str__(self):
        return self.subcompetency_name

    #sub_competency = models.ForeignKey(Competency, on_delete=models.CASCADE, related_name='role')
    subcompetency_name = models.CharField(max_length=250, unique=True)



class Sub_Competency1(models.Model):
    def __str__(self):
        return self.name

    name = models.CharField(max_length=250, unique=True)
    power_words = models.ManyToManyField(PowerWords1, blank=True)
    negative_words = models.ManyToManyField(NegativeWords1, blank=True)
    emotion_words = models.ManyToManyField(EmotionWords, blank=True)

    

class Competency(models.Model):
    def __str__(self):
        return self.competency_name

    competency_name = models.CharField(max_length = 250, unique=True)
    sub_competency = models.ManyToManyField(Sub_Competency, blank=True)

class Competency1(models.Model):
    def __str__(self):
        return self.competency_name

    competency_name = models.CharField(max_length = 250, unique=True)
    sub_competency = models.ManyToManyField(Sub_Competency1, blank=True)