# Generated by Django 4.2.4 on 2023-09-27 11:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orgss', '0002_weightage_role_competency_and_more'),
        ('accounts', '0013_alter_account_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='role',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='orgss.org_roles'),
        ),
    ]
