# Generated by Django 5.0.2 on 2024-03-19 08:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_rename_name_userrights_rights'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userrightsmapping',
            old_name='right',
            new_name='rights',
        ),
    ]