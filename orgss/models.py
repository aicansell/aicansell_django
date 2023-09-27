from django.db import models
from industry.models import Industry

from role.models import Roles, Sub_Role
from competency.models import Competency, Sub_Competency
#from sean.models import Item

#from quiz.models import Quiz

# Create your models here.
class Org(models.Model):
    def __str__(self):
        return self.name

    name = models.CharField(max_length=250)
    description = models.CharField(max_length=500, blank=True, null=True)
    industry1 = models.ForeignKey(Industry, on_delete=models.CASCADE, related_name='industry1')


class Org_Roles(models.Model):
    def __str__(self):
        return self.org_role_name

    org_role_name = models.CharField(max_length=250, blank=True, null=True)
    org = models.ForeignKey(Org, on_delete=models.CASCADE, default = 1, related_name='org1')
    role = models.ForeignKey(Roles, on_delete=models.CASCADE, default = 1, related_name='roles12')
    subrole = models.ForeignKey(Sub_Role, on_delete=models.CASCADE, default = 1, related_name='org1')
    

class Weightage(models.Model):
    org_role = models.ForeignKey(Org_Roles, on_delete=models.CASCADE)
    role_competency = models.ForeignKey(Competency, on_delete=models.CASCADE, default=1, related_name= 'rolecompetency1')
    #subcompetencys = models.ForeignKey(Sub_Competency, on_delete=models.CASCADE, default=1)
    subcompetency = models.ManyToManyField(Sub_Competency, blank=True)
    weight = models.IntegerField(default=1)
    
    def __str__(self):
        return f'{self.role_competency}'
    
    
    
"""
class Role_Scenario(models.Model):
    def __str__(self):
        return self.role_scenario_name

    role_scenario_name = models.CharField(max_length=250, blank=True, null=True)
    role_scenario = models.ForeignKey(Org_Roles, on_delete=models.CASCADE, default=1, related_name= 'rolescenario')
    rolescenario_item = models.ForeignKey(Item, on_delete=models.CASCADE, default=1, related_name= 'rolescenario_item')

"""
