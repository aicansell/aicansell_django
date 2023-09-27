from django.db import models


class Sub_Competency(models.Model):
    def __str__(self):
        return self.name

    name = models.CharField(max_length=250, unique=True)

    

class Competency(models.Model):
    def __str__(self):
        return self.name

    name = models.CharField(max_length = 250, unique=True)
    sub_competency = models.ManyToManyField(Sub_Competency, blank=True)

    

