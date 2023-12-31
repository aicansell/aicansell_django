from django.db import models
from industry.models import Industry

from competency.models import Competency

class Org(models.Model):
    def __str__(self):
        return self.name

    name = models.CharField(max_length=250)
    description = models.CharField(max_length=500, blank=True, null=True)
    industry = models.ForeignKey(Industry, on_delete=models.CASCADE, related_name='industry', default = 1)


class Org_Roles(models.Model):
    def __str__(self):
        return self.org_role_name

    org_role_name = models.CharField(max_length=250, blank=True, null=True)
    org = models.ForeignKey(Org, on_delete=models.CASCADE, default = 1, related_name='org')


class Weightage(models.Model):
    org_role = models.ForeignKey(Org_Roles, on_delete=models.CASCADE)
    competency = models.ForeignKey(Competency, on_delete=models.CASCADE, default=1, related_name= 'rolecompetency')
    weightage = models.IntegerField(default=1)
    
    def __str__(self):
        return f'{self.competency}'
