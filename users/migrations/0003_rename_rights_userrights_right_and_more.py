# Generated by Django 5.0.2 on 2024-03-19 09:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_userrights_userrightsmapping'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userrights',
            old_name='rights',
            new_name='right',
        ),
        migrations.RenameField(
            model_name='userrightsmapping',
            old_name='rights_name',
            new_name='right',
        ),
    ]
