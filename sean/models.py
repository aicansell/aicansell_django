from django.db import models
#from organisation.models import Org_Roles
from orgss.models import Org_Roles
from accounts.models import Account
from competency.models import Competency


class Traits(models.Model):
    def __str__(self):
        return self.trait_name

    trait_name = models.CharField(max_length=250, default= "trait")

class Collection(models.Model):
    def __str__(self):
        return self.trait_name

    collection_name = models.CharField(max_length=250, default= "collection")    


class Item(models.Model):
    def __str__(self):
        return self.item_name

    Gender1 = "Female"
    Gender2 = "Male"   
    Gender3 = "All" 

    Type1 = "Simulation"
    Type2 = "Email"

    item_name = models.CharField(max_length=256)
    item_description = models.CharField(max_length=300, blank=True, null = True)
   
    item_answer = models.TextField(max_length=700, default="Your answer")
    item_emotion = models.TextField(default= "emotions")
    item_answercount = models.IntegerField(default=1)
    category = models.CharField(max_length=256, blank=True, default="Personal")
    thumbnail = models.ImageField(upload_to='media', default = "c.png")  
    #power_words = models.CharField(max_length=300, default="Tip")
    #weak_words = models.CharField(max_length=300, default='appear')
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
    role = models.ForeignKey(Org_Roles, on_delete=models.CASCADE, blank=True, null=True)
    coming_across_as = models.CharField(max_length=250, default="sugestions")
    #competency = models.ForeignKey(Competency, on_delete=models.CASCADE, default=1, blank=True)
    #sub_competency = models.ForeignKey(Sub_Competency, on_delete = models.CASCADE, default= 1, blank=True)
    competencys = models.ManyToManyField(Competency, blank=True)
    #seans_recommendation = models.CharField(max_length=300, default= "improve on")
    level = models.IntegerField(default=1)
    positive_traits = models.CharField(max_length=300, default=" ", blank=True)
    negative_traits = models.CharField(max_length=300, default=" ", blank = True)
    user_powerwords = models.CharField(max_length=300, default="")
    user_weakwords = models.CharField(max_length=300, default="")
    expert = models.FileField(upload_to='media', blank = True, null=True)



class Suggestion(models.Model):
    def __str__(self):
        return self.suggestion_text

    name = models.CharField(max_length=256)
    suggestion_text = models.TextField()

