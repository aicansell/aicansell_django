from django.db import models
from role.models import Roles, Sub_Role
from organisation.models import Org_Roles
from competency.models import Competency, Sub_Competency
from words.models import Words



# Create your models here.

class PowerWords(models.Model):
    def __str__(self):
        return f'{self.word}'

    
    word = models.ForeignKey(Words, on_delete=models.CASCADE, default=1)
    competency = models.ForeignKey(Competency, on_delete=models.CASCADE, default=1)
    sub_competency = models.ForeignKey(Sub_Competency, on_delete = models.CASCADE, default= 1)
    org_role = models.ForeignKey(Org_Roles, on_delete=models.CASCADE, default=1)
    weight = models.IntegerField(default=1)
    sentence = models.CharField(max_length=250, default= "sentence")
    power_word_name = models.CharField(max_length=250)
    

class NegativeWords(models.Model):
    def __str__(self):
         return f'{self.word}'

    
    word = models.ForeignKey(Words, on_delete=models.CASCADE, default=1)
    competencys = models.ForeignKey(Competency, on_delete=models.CASCADE, default=1)
    sub_competency = models.ForeignKey(Sub_Competency, on_delete = models.CASCADE, default= 1)
    org_role = models.ForeignKey(Org_Roles, on_delete=models.CASCADE, default=1)
    weight = models.IntegerField(default= -7)
    sentence = models.CharField(max_length=250, default= "sentence")
    negative_word_name = models.CharField(max_length=250)

class EmotionWords(models.Model):
    def __str__(self):
        return f'{self.word}'

    word = models.ForeignKey(Words, on_delete=models.CASCADE, default=1)
    emotion_word_name = models.CharField(max_length=250)
    competency = models.ForeignKey(Competency, on_delete=models.CASCADE, default=1)
    sub_competency = models.ForeignKey(Sub_Competency, on_delete = models.CASCADE, default= 1)
    org_role = models.ForeignKey(Org_Roles, on_delete=models.CASCADE, default=1)
    


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
   
    
    #item_role = models.ForeignKey(Roles, on_delete = models.CASCADE, default=1, related_name = 'itemrole')
    #item_subrole = models.ForeignKey(Sub_Role, on_delete = models.CASCADE, default=1, related_name = 'itemsubrole')
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
    role = models.ForeignKey(Org_Roles, on_delete=models.CASCADE, default=1)
    coming_across_as = models.CharField(max_length=250, default="sugestions")
    #competency = models.ForeignKey(Competency, on_delete=models.CASCADE, default=1, blank=True)
    #sub_competency = models.ForeignKey(Sub_Competency, on_delete = models.CASCADE, default= 1, blank=True)
    competency = models.ManyToManyField(Competency, blank=True)
    sub_competency = models.ManyToManyField(Sub_Competency, blank=True)
    #seans_recommendation = models.CharField(max_length=300, default= "improve on")
    competency_power_words = models.ManyToManyField(PowerWords, blank=True, limit_choices_to={'competency':True})
    competency_weak_words = models.ManyToManyField(NegativeWords, blank=True, limit_choices_to={'competency':True})
    competency_emotion_word = models.ForeignKey(EmotionWords, on_delete = models.CASCADE, default= 1)
    level = models.IntegerField(default=1)
    positive_traits = models.CharField(max_length=300, default=" ", blank=True)
    negative_traits = models.CharField(max_length=300, default=" ", blank = True)
    user_powerwords = models.CharField(max_length=300, default="up")
    user_weakwords = models.CharField(max_length=300, default="unp")
    expert = models.FileField(upload_to='media', blank = True, null=True)
    


class Suggestion(models.Model):
    def __str__(self):
        return self.suggestion_text

    name = models.CharField(max_length=256)
    suggestion_text = models.TextField()

