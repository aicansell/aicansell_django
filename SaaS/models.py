from django.db import models

from accounts.models import Account

class Feature(models.Model):
    FREQUENCY = (
        ('unlimited', 'Unlimited'),
        ('annual', 'Annual'),
        ('monthly', 'Monthly'),
        ('weekly', 'Weekly'),
    )
    
    name = models.CharField(max_length=300)
    price = models.DecimalField(max_digits=20, decimal_places=2, default=0.00)
    frequency = models.CharField(max_length=100, choices=FREQUENCY, default='unlimited')
    description = models.TextField(null=True, blank=True)
    
    def __str__(self):
        return f"{self.name} - {self.price}"
    
class FeatureList(models.Model):
    FREQUENCY = (
        ('unlimited', 'Unlimited'),
        ('day', 'Day'),
        ('week', 'Week'),
        ('month', 'month'),
    )
    
    feature = models.ForeignKey(Feature, on_delete=models.CASCADE)
    name = models.CharField(max_length=300)
    frequency = models.CharField(max_length=100, choices=FREQUENCY, null=True, blank=True)
    times = models.IntegerField(default=1)
    
    def __str__(self):
        return f"{self.name} - {self.feature.name} - {self.times}"

class SaaS(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    feature = models.ForeignKey(Feature, on_delete=models.CASCADE)
    startdate = models.DateField(auto_now_add=True)
    enddate = models.DateField(null=True, blank=True)
    
    def __str__(self):
        return f"{self.user.username} - {self.feature.name}"
    
    class Meta:
        unique_together = ["user", "feature"]
