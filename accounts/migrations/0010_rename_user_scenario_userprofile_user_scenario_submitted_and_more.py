# Generated by Django 4.2.4 on 2023-09-14 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_userprofile_user_scenario'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='user_scenario',
            new_name='user_scenario_submitted',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='city',
            field=models.CharField(default='', max_length=250),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='level',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='user_scenario_bookmarked',
            field=models.CharField(default='', max_length=250),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='user_scenario_saved',
            field=models.CharField(default='', max_length=250),
        ),
    ]
