from django.db import models

# Create your models here.
class Role(models.Model):
    def __str__(self):
        return self.name

    name = models.CharField(max_length = 250)

class Sub_Role(models.Model):
    def __str__(self):
        return self.subrole

    role = models.ForeignKey(Role, on_delete=models.CASCADE, related_name='role')
    subrole = models.CharField(max_length=250)
 