from django.db import models

from competency.models import Competency
from accounts.models import Account

class SnakeLadderGame(models.Model):
    name = models.CharField(max_length=100)
    competency = models.ForeignKey(Competency, on_delete=models.CASCADE)
    description = models.TextField()
    thumbnail = models.FileField(upload_to='media/game/snakeladdergame/thumbnail', null=True, blank=True)

    def __str__(self):
        return self.name
    
class Questions(models.Model):
    snakeladdergame = models.ForeignKey(SnakeLadderGame, on_delete=models.CASCADE)
    question = models.TextField()
    thumbnail = models.FileField(upload_to='media/question/snakeladdergame/question', null=True, blank=True)
    timer = models.IntegerField(default=0)
    
    def __str__(self):
        return self.question
    
class Options(models.Model):
    question = models.ForeignKey(Questions, on_delete=models.CASCADE)
    option = models.CharField(max_length=300)
    point = models.IntegerField(default=0)
    
    def __str__(self):
        return self.option
    
class SnakeLadderGameResult(models.Model):
    snakeladdergame = models.ForeignKey(SnakeLadderGame, on_delete=models.CASCADE)
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    score = models.IntegerField(default=0)
    created_at = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.snakeladdergame.name + ' - ' + self.user.username

    class Meta:
        unique_together = ('snakeladdergame', 'user')
