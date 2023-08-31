from django.db import models
from organisation.models import Org, Org_Roles



# Create your models here.
class Option(models.Model):
    def __str__(self):
        return self.option_text

    option_text = models.CharField(max_length=300)

class YourAnswer(models.Model):
    def __str__(self):
        return self.answer_name

    answer_name = models.CharField(max_length=10)          

class Feedback(models.Model):
    def __str__(self):
        return self.feedback_text

    feedback_text = models.CharField(max_length=500)        

class Quiz(models.Model):
    def __str__(self):
        return self.item_name

    Option1 = "Opt1"
    Option2 = "Opt2"
    Option3 = "Opt3"

    item_name = models.CharField(max_length= 500)
    
    option1 = models.ForeignKey(Option, on_delete=models.CASCADE, related_name='opt1') 
    option1_weight = models.IntegerField(default=1)
    option2 = models.ForeignKey(Option, on_delete=models.CASCADE, related_name='opt2')   
    option2_weight = models.IntegerField(default=1)
    option3 = models.ForeignKey(Option, on_delete=models.CASCADE, related_name='opt3')    
    option3_weight = models.IntegerField(default=1)
    feedback1 = models.ForeignKey(Feedback, on_delete=models.CASCADE, related_name='fdb1')
    feedback2 = models.ForeignKey(Feedback, on_delete=models.CASCADE, related_name='fdb2')
    feedback3 = models.ForeignKey(Feedback, on_delete=models.CASCADE, related_name='fdb3')
    answer_count = models.IntegerField(default=1)
    
    QuizAnswer_CHOICES = [
        (Option1, "Option 1"),
        (Option2, "Option 2"),
        (Option3, "Option 3"),
    ]
    answer = models.CharField(
        max_length=4,
        choices=QuizAnswer_CHOICES,
        default=Option1,
    )
    
    
class Quiz_Roles(models.Model):
    def __str__(self):
        return self.quiz_orgname

    quiz_orgname = models.CharField(max_length= 500)
    quizquestion_name = models.ForeignKey(Quiz, on_delete=models.CASCADE, default=1, related_name='quiz')
    quiz_org_name = models.ForeignKey(Org, on_delete=models.CASCADE, related_name='org4')
    quiz_org_role = models.ForeignKey(Org_Roles, on_delete=models.CASCADE, related_name='role4')
