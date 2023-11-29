from django.db import models

from accounts.models import Account


class IceBreaker(models.Model):
    going_for = models.CharField(max_length=200, null=True, blank=True)
    with_who = models.CharField(max_length=200, null=True, blank=True)
    help_on = models.CharField(max_length=200, null=True, blank=True)
    come_across_as = models.CharField(max_length=200, null=True, blank=True)
    not_come_across_as = models.CharField(max_length=200, null=True, blank=True)
    created_by = models.ForeignKey(Account, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.created_by.first_name} - {self.going_for} - {self.with_who}"

    class Meta:
        verbose_name_plural = "IceBreakers"
        ordering = ["-created_at"]

class IndividualInputScenarios(models.Model):
    going_for = models.CharField(max_length=200, null=True, blank=True)
    with_who = models.CharField(max_length=200, null=True, blank=True)
    help_on = models.CharField(max_length=200, null=True, blank=True)
    come_across_as = models.CharField(max_length=200, null=True, blank=True)
    not_come_across_as = models.CharField(max_length=200, null=True, blank=True)
    created_by = models.ForeignKey(Account, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.created_by.first_name} - {self.going_for} - {self.with_who}"

    class Meta:
        verbose_name_plural = "Individual Input Scenarios"
        ordering = ["-created_at"]
