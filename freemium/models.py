from django.db import models
from accounts.models import Account;

class Freemium(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    duration = models.CharField(max_length=50, choices=[('per_month', 'Per Month'), ('per_interaction', 'Per Interaction')])
    access = models.CharField(max_length=50, choices=[('unlimited', 'Unlimited'), ('limited', 'Limited'), ('one_time','One_Time')])
    access_time = models.DurationField(null=True)

    def __str__(self):
        return self.name
    
class Subscription(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    service = models.ForeignKey(Freemium, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    is_expired = models.BooleanField(default=False)

    def __str__(self):
        return self.service.name
