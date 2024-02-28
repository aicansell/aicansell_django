from django.db import models

from accounts.models import Account
from orgss.models import SubOrg

class UserSubOrgs(models.Model):
    user = models.ForeignKey(Account, on_delete=models.SET_NULL, null=True, related_name='user_suborgs')
    suborg = models.ForeignKey(SubOrg, on_delete=models.SET_NULL, null=True, related_name='suborg_users')
    
    def __str__(self):
        return self.user.username + ' - ' + self.suborg.name + ' - ' + self.user.role.name

class UserMapping(models.Model):
    admin = models.ForeignKey(Account, on_delete=models.SET_NULL, null=True, related_name='admin_manager')
    user = models.ForeignKey(Account, on_delete=models.SET_NULL, null=True, related_name='mapped_user')
    
    def __str__(self):
        return self.superadmin.username + ' - ' + self.admin.username
