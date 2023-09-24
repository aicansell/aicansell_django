# Generated by Django 4.2.4 on 2023-09-23 12:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('organisation', '0006_remove_org_roles_competency_weight_and_more'),
        ('accounts', '0013_alter_account_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='role',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='organisation.org_roles'),
        ),
    ]