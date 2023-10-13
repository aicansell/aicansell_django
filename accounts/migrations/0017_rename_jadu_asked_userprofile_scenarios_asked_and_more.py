# Generated by Django 4.2.4 on 2023-10-13 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0016_account_user_role_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='jadu_asked',
            new_name='scenarios_asked',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='jadu_attempted',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='user_scenario_bookmarked',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='user_scenario_submitted',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='pw_competency',
            field=models.CharField(default='pw', max_length=250),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='scenario_attempt_pw',
            field=models.CharField(default='sapw', max_length=250),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='scenario_attempt_ww',
            field=models.CharField(default='saww', max_length=250),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='user_powerwords',
            field=models.CharField(default='upw', max_length=250),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='user_weakwords',
            field=models.CharField(default='uww', max_length=250),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='ww_competency',
            field=models.CharField(default='ww', max_length=250),
        ),
    ]
