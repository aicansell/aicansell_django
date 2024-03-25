from SaaS.models import SaaS, Feature

from datetime import datetime

def check_subcription_of_users():
    downgrade_users = SaaS.objects.filter(enddate__lt=datetime.now(), feature__name__icontains="premium")
    downgrade_users.update(feature=Feature.objects.filter(name__icontains="free").first(), enddate=None)
