from django.db import models
from role.models import Roles, Sub_Role
#from organisation.models import Org


# Create your models here.

class Item(models.Model):
    def __str__(self):
        return self.item_name

    Gender1 = "Female"
    Gender2 = "Male"   
    Gender3 = "All" 

    item_name = models.CharField(max_length=256)
    item_description = models.CharField(max_length=300)
   

    #item_role = models.ForeignKey(Roles, on_delete = models.CASCADE, default=1, related_name = 'itemrole')
    #item_subrole = models.ForeignKey(Sub_Role, on_delete = models.CASCADE, default=1, related_name = 'itemsubrole')
    item_answer = models.TextField(max_length=700, default="Your answer")
    item_emotion = models.TextField(default= "emotions")
    item_answercount = models.IntegerField(default=1)
    category = models.CharField(max_length=256, blank=True, default="Personal")
    thumbnail = models.ImageField(upload_to='media', default = "c.png")  
    tip = models.CharField(max_length=300, default="Tip")
    appearance = models.CharField(max_length=300, default='appear')
    Gender_CHOICES = [
        (Gender1, "Gender 1"),
        (Gender2, "Gender 2"),
        (Gender3, "Gender 3"),
    ]
    item_gender = models.CharField(max_length=7, choices = Gender_CHOICES, default=Gender1)


class Suggestion(models.Model):
    def __str__(self):
        return self.suggestion_text

    name = models.CharField(max_length=256)
    suggestion_text = models.TextField()