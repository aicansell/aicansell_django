# Generated by Django 4.2.4 on 2023-10-04 05:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('competency', '0006_competency1'),
        ('words', '0002_powerwords_negativewords_emotionwords'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='NegativeWords',
            new_name='NegativeWords1',
        ),
        migrations.RenameModel(
            old_name='PowerWords',
            new_name='PowerWords1',
        ),
    ]
