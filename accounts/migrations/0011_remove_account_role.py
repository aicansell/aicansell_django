# Generated by Django 4.2.4 on 2023-09-20 05:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0010_rename_user_scenario_userprofile_user_scenario_submitted_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='role',
        ),
    ]