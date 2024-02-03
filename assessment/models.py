from django.db import models

class Style(models.Model):
    name = models.CharField(max_length=100)
    msg = models.TextField(null=True, blank=True)
    
    def __str__(self):
        return self.name
    
class Situation(models.Model):
    name = models.CharField(max_length=500)
    style = models.ForeignKey(Style, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
    
class Assessment1(models.Model):
    optionA = models.ForeignKey(Situation, on_delete=models.CASCADE, related_name='optionA')
    optionB = models.ForeignKey(Situation, on_delete=models.CASCADE, related_name='optionB')
    
    def __str__(self):
        return f'{self.optionA.name} {self.optionB.name}'

class Assessment2(models.Model):
    optionA = models.ForeignKey(Situation, on_delete=models.CASCADE, related_name='optionA2')
    optionB = models.ForeignKey(Situation, on_delete=models.CASCADE, related_name='optionB2')
    
    def __str__(self):
        return f'{self.optionA.name} {self.optionB.name}'

class Assessment3(models.Model):
    choice = models.CharField(max_length=500)
    
    def __str__(self):
        return self.choice[:200]
