# Generated by Django 4.2.4 on 2023-10-11 04:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('competency', '0010_remove_competency_sub_competency'),
        ('organisation', '0007_remove_org_roles_role_subcompetency'),
    ]

    operations = [
        migrations.AlterField(
            model_name='org_roles',
            name='role_competency',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='rolecompetency', to='competency.competency1'),
        ),
        migrations.AlterField(
            model_name='org_roles',
            name='role_subcompetencys',
            field=models.ManyToManyField(blank=True, to='competency.sub_competency1'),
        ),
    ]
