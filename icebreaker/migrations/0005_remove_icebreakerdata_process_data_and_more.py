# Generated by Django 4.2.4 on 2024-01-05 06:52

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("icebreaker", "0004_icebreakerdata"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="icebreakerdata",
            name="process_data",
        ),
        migrations.AddField(
            model_name="icebreakerdata",
            name="ice_breakers",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="icebreakerdata",
            name="interests",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="icebreakerdata",
            name="profile_pic_url",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="icebreakerdata",
            name="summary_and_facts",
            field=models.TextField(blank=True, null=True),
        ),
    ]
