from django.core.management.base import BaseCommand
from sean.models import PowerWords
from words.models import PowerWords

class Command(BaseCommand):
    help = 'Transfer data from OldModel to NewModel'

    def handle(self, *args, **kwargs):
        old_data = PowerWords.objects.all()

        for item in old_data:
            new_item = PowerWords(
                word=item.word,
                weight=item.weight,
                sentence = item.sentence,
                power_word_name = item.power_word_name
                # Copy other fields as needed
            )
            new_item.save()