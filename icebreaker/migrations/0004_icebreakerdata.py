# Generated by Django 4.2.4 on 2024-01-04 18:04

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        (
            "icebreaker",
            "0003_rename_going_for_individualinputscenarios_need_help_on_and_more",
        ),
    ]

    operations = [
        migrations.CreateModel(
            name="IceBreakerData",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("username", models.CharField(blank=True, max_length=200, null=True)),
                ("process_data", models.TextField()),
            ],
        ),
    ]