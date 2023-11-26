from django.db import models

from words.models import PowerWords, WeakWords

class Scenarios(models.Model):
    item_name = models.CharField(max_length=300)
    item_emotions = models.TextField()
    power_words = models.ManyToOneRel(PowerWords, on_delete=models.CASCADE)
    weak_words = models.ManyToOneRel(WeakWords, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.item_name
    
    class Meta:
        verbose_name_plural = "Scenarios"
