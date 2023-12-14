from django.db import models

from words.models import PowerWords, NegativeWords

class Scenarios(models.Model):
    item_name = models.CharField(max_length=300)
    item_emotions = models.TextField(null=True, blank=True)
    own_scenarios = models.TextField(null=True, blank=True)
    power_words = models.ManyToManyField(PowerWords, blank=True)
    negative_words = models.ManyToManyField(NegativeWords, blank=True)
    
    def __str__(self):
        return self.item_name
    
    class Meta:
        verbose_name_plural = "Scenarios"
