from django.db import models

from competency.models import Competency

class Situations(models.Model):
    situation = models.TextField()

    def __str__(self):
        return self.situation
    
class Interest(models.Model):
    interest = models.CharField(max_length=200)

    def __str__(self):
        return self.interest
    
class Tags(models.Model):
    tag = models.CharField(max_length=100)

    def __str__(self):
        return self.tag
    
class SeanScenarios(models.Model):
    scenario = models.CharField(max_length=1000)
    scenario_answer = models.TextField(null=True, blank=True)
    scenario_answer_count = models.IntegerField(default=0)
    thumbnail = models.FileField(upload_to='media/scenarios/thumbnail', blank=True, null=True)
    level = models.IntegerField(default=0)
    competency = models.ManyToManyField(Competency, blank=True)
    
    def get_competency_as_string(self):
        return ", ".join(self.competency.values_list('competency_name', flat=True))
    
    def __str__(self):
        return self.scenario

class SeanScenariosSituations(models.Model):
    scenario = models.ForeignKey(SeanScenarios, on_delete=models.CASCADE)
    situation = models.ForeignKey(Situations, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.scenario.scenario + " - " + self.situation.situation
    
class SeanScenariosInterests(models.Model):
    scenario = models.ForeignKey(SeanScenarios, on_delete=models.CASCADE)
    interest = models.ForeignKey(Interest, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.scenario.scenario + " - " + self.interest.interest
    
class SeanScenariosTags(models.Model):
    scenario = models.ForeignKey(SeanScenarios, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tags, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.scenario.scenario + " - " + self.tag.tag
