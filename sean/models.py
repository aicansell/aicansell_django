from django.db import models
from role.models import Roles, Sub_Role
#from organisation.models import Org_Roles
from orgss.models import Org_Roles
from competency.models import Competency, Sub_Competency
from words.models import Words

from accounts.models import Account


# Create your models here.


class Item(models.Model):
    def __str__(self):
        return self.item_name

    Gender1 = "Female"
    Gender2 = "Male"   
    Gender3 = "All" 

    Type1 = "Simulation"
    Type2 = "Email"

    Scenario_Type1 = "Sales"
    Scenario_Type2 = "Customer Service"
    Scenario_Type3 = "Interview"


    item_name = models.CharField(max_length=700)
    item_description = models.CharField(max_length=300, blank=True, null = True)
   
    item_answer = models.TextField(max_length=700, default="Your answer")
    item_emotion = models.TextField(default= "emotions")
    item_answercount = models.IntegerField(default=1)
    category = models.CharField(max_length=256, blank=True, default="Personal")
    thumbnail = models.ImageField(upload_to='media', default = "c.png")  
    
    Gender_CHOICES = [
        (Gender1, "Female"),
        (Gender2, "Male"),
        (Gender3, "All"),
    ]
    item_gender = models.CharField(max_length=7, choices = Gender_CHOICES, default=Gender3)
    Type_CHOICES = [
        (Type1, "Simulation"),
        (Type2, "Email")
    ]
    item_type = models.CharField(max_length=16, choices = Type_CHOICES, default=Type1)
    Scenario_Type_CHOICES = [
        (Scenario_Type1, "Sales"),
        (Scenario_Type2, "Customer Service"),
        (Scenario_Type3, "Interview"),
        
    ]
    scenario_type = models.CharField(max_length= 16, choices = Scenario_Type_CHOICES, default= Scenario_Type1)
    role = models.ForeignKey(Org_Roles, on_delete=models.CASCADE, default=1)
    coming_across_as = models.CharField(max_length=250, default="sugestions")
    
    competencys = models.ManyToManyField(Competency, blank=True)
    #competency_power_words = models.ManyToManyField(PowerWords, blank=True)
    #competency_weak_words = models.ManyToManyField(NegativeWords, blank=True)
    level = models.IntegerField(default=1)
    positive_traits = models.CharField(max_length=300, default=" ", blank=True)
    negative_traits = models.CharField(max_length=300, default=" ", blank = True)
    user_powerwords = models.CharField(max_length=300, default="up")
    user_weakwords = models.CharField(max_length=300, default="unp")
    expert = models.FileField(upload_to='media', blank = True, null=True)

    def get_competencys_as_string(self):
        return ', '.join(self.competencys.values_list('competency_name', flat=True))
    


class Suggestion(models.Model):
    def __str__(self):
        return self.suggestion_text

    name = models.CharField(max_length=256)
    suggestion_text = models.TextField()