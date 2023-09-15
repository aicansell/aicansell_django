from django.db import models

# Create your models here.
class Words(models.Model):
    def __str__(self):
        return self.word_name

    word_name = models.CharField(max_length=250)