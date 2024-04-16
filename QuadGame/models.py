from django.db import models

from accounts.models import Account
from competency.models import Competency

class QuadGame(models.Model):
    name = models.CharField(max_length=100)
    thubmnail = models.FileField(upload_to='quadgame/thumbnail/', null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    competency = models.ForeignKey(Competency, on_delete=models.CASCADE)
    postive_marks = models.IntegerField(default=0)
    negative_marks = models.IntegerField(default=0)

    def __str__(self):
        return self.name

class Quadrant(models.Model):
    name = models.CharField(max_length=100)
    thubmnail = models.FileField(upload_to='quadrant/thumbnail/', null=True, blank=True)
    quadgame = models.ForeignKey(QuadGame, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
class Statements(models.Model):
    statement = models.TextField()
    thumbnail = models.FileField(upload_to='statements/thumbnail/', null=True, blank=True)
    quadrant = models.ForeignKey(Quadrant, on_delete=models.CASCADE)

    def __str__(self):
        return self.statement

class Questions(models.Model):
    question = models.TextField()
    thumbnail = models.FileField(upload_to='questions/thumbnail/', null=True, blank=True)
    quadgame = models.ForeignKey(QuadGame, on_delete=models.CASCADE)
    statements = models.ManyToManyField(Statements)
    timer = models.IntegerField(default=0)

    def __str__(self):
        return self.question

class QuadGameResult(models.Model):
    quadgame = models.ForeignKey(QuadGame, on_delete=models.CASCADE)
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    score = models.IntegerField(default=0)
    created_at = models.DateField(auto_now_add=True)
    
    class Meta:
        unique_together = ('quadgame', 'user',)

    def __str__(self):
        return f"{self.user.username} - {self.score}"
