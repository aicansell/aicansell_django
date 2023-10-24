from django.core.management.base import BaseCommand
from competency.models import Sub_Competency, Sub_Competency1
#from words.models import PowerWords1, NegativeWords1

class Command(BaseCommand):
    help = 'Transfer data from OldModel to NewModel'

    def handle(self, *args, **kwargs):
        old_data = Sub_Competency.objects.all()

        for item in old_data:
            new_item = Sub_Competency1(
                name=item.subcompetency_name,
                
                # Copy other fields as needed
            )
            new_item.save()
