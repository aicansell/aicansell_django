# Generated by Django 4.2.4 on 2024-02-22 17:04

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("industry", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="industry",
            old_name="industry_description",
            new_name="description",
        ),
        migrations.RemoveField(
            model_name="industry",
            name="industry_name",
        ),
        migrations.AddField(
            model_name="industry",
            name="name",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
