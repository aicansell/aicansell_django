# Generated by Django 4.2.6 on 2023-10-19 14:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('competency', '0002_competency_competency_sentiment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='competency',
            old_name='name',
            new_name='competency_name',
        ),
    ]
