from django.db import models
from industry.models import Industry

from role.models import Role, Sub_Role
from competency.models import Competency, Sub_Competency
#from sean.models import Item

#from quiz.models import Quiz

# Create your models here.
class Org(models.Model):
    def __str__(self):
        return self.name

    name = models.CharField(max_length=250)
    description = models.CharField(max_length=500, blank=True, null=True)
    industry = models.ForeignKey(Industry, on_delete=models.CASCADE, related_name='industry')


class Org_Roles(models.Model):
    def __str__(self):
        return self.org_role_name

    org_role_name = models.CharField(max_length=250, blank=True, null=True)
    org = models.ForeignKey(Org, on_delete=models.CASCADE, default = 1, related_name='org1')
    role = models.ForeignKey(Role, on_delete=models.CASCADE, default = 1, related_name='roles1')
    subrole = models.ForeignKey(Sub_Role, on_delete=models.CASCADE, default = 1, related_name='org')
    

class Weightage(models.Model):
    org_role = models.ForeignKey(Org_Roles, on_delete=models.CASCADE)
    subcompetency = models.ForeignKey(Sub_Competency, on_delete=models.CASCADE, default=1)
    weight = models.IntegerField(default=1)
    
    def __str__(self):
        return self.subcompetency
    
    
    
"""
class Role_Scenario(models.Model):
    def __str__(self):
        return self.role_scenario_name

    role_scenario_name = models.CharField(max_length=250, blank=True, null=True)
    role_scenario = models.ForeignKey(Org_Roles, on_delete=models.CASCADE, default=1, related_name= 'rolescenario')
    rolescenario_item = models.ForeignKey(Item, on_delete=models.CASCADE, default=1, related_name= 'rolescenario_item')

"""