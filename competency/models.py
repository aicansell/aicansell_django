from django.db import models

# Create your models here.

class Sub_Competency(models.Model):
    def __str__(self):
        return self.subcompetency_name

    #sub_competency = models.ForeignKey(Competency, on_delete=models.CASCADE, related_name='role')
    subcompetency_name = models.CharField(max_length=250, unique = True)

    def clean(self):
        existing_entries = Sub_Competency.objects.exclude(id=self.id)
        if existing_entries.filter(unique_field=self.unique_field).exists():
            raise ValidationError({'unique_field': 'This field must be unique.'})

class Competency(models.Model):
    def __str__(self):
        return self.competency_name

    competency_name = models.CharField(max_length = 250, unique=True)
    sub_competency = models.ManyToManyField(Sub_Competency, blank=True)

    

