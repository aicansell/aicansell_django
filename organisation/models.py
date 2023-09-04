from django.db import models
from industry.models import Industry

from role.models import Roles, Sub_Role
from competency.models import Competency, Sub_Competency
from sean.models import Item

#from quiz.models import Quiz

# Create your models here.
class Org(models.Model):
    def __str__(self):
        return self.org_name

    org_name = models.CharField(max_length=250)
    org_description = models.CharField(max_length = 500, blank = True)
    org_industry = models.ForeignKey(Industry, on_delete=models.CASCADE, related_name='industry')


class Org_Roles(models.Model):
    def __str__(self):
        return self.org_role_name

    org_role_name = models.CharField(max_length=250, blank=True, null=True)
    org_na =  models.ForeignKey(Org, on_delete=models.CASCADE, default = 1, related_name='org1')
    org_role = models.ForeignKey(Roles, on_delete=models.CASCADE, default = 1, related_name='roles1')
    subrole_org = models.ForeignKey(Sub_Role, on_delete=models.CASCADE, default = 1, related_name='org')
    role_competency = models.ForeignKey(Competency, on_delete=models.CASCADE, default=1, related_name= 'rolecompetency')
    competency_weight = models.IntegerField(default = 1)
    role_subcompetency = models.ForeignKey(Sub_Competency, on_delete=models.CASCADE, default=1, related_name = 'rolesubcompetency')
    subcompetency_weight = models.IntegerField(default=1)

class Role_Scenario(models.Model):
    def __str__(self):
        return self.role_scenario_name

    role_scenario_name = models.CharField(max_length=250, blank=True, null=True)
    role_scenario = models.ForeignKey(Org_Roles, on_delete=models.CASCADE, default=1, related_name= 'rolescenario')




 
