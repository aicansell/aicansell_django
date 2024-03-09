from django.db import models

from accounts.models import Account
from series.models import Series

class SeriesAssignUser(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    series = models.ForeignKey(Series, on_delete=models.CASCADE)
    is_completed = models.BooleanField(default=False)
    progress = models.IntegerField(default=0)

    class Meta:
        unique_together = ["user", "series"]

    def __str__(self):
        return f"{self.user.username} - {self.series.name}"
