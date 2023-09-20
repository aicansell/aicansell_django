from django.db import models

# Create your models here.

class Sub_Competency(models.Model):
    def __str__(self):
        return self.subcompetency_name

    #sub_competency = models.ForeignKey(Competency, on_delete=models.CASCADE, related_name='role')
    subcompetency_name = models.CharField(max_length=250)

class Competency(models.Model):
    def __str__(self):
        return self.competency_name

    competency_name = models.CharField(max_length = 250)
    sub_competency = models.ManyToManyField(Sub_Competency, blank=True, limit_choices_to={'subcompetency_name':True})

