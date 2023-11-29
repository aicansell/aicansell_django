from django.db import models

class Freemium(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    duration = models.CharField(max_length=50, choices=[('per_month', 'Per Month'), ('per_interaction', 'Per Interaction')])
    access = models.CharField(max_length=50, choices=[('unlimited', 'Unlimited'), ('limited', 'Limited')])

    def __str__(self):
        return self.name
