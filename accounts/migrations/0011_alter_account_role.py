# Generated by Django 4.2.4 on 2023-09-20 05:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('organisation', '0005_delete_role_scenario'),
        ('accounts', '0010_rename_user_scenario_userprofile_user_scenario_submitted_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='role',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='userorg1', to='organisation.org_roles'),
        ),
    ]
