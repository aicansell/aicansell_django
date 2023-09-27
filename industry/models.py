from django.db import models

# Create your models here.
class Industry(models.Model):
    def __str__(self):
        return self.industry_name

    industry_name = models.CharField(max_length = 300)
    industry_description = models.CharField(max_length = 500, blank=True, null=True)
