# Generated by Django 4.2.6 on 2023-10-19 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_account_role'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='role',
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