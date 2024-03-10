# Generated by Django 5.0.2 on 2024-03-08 16:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Question",
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
                ("question", models.CharField(max_length=200)),
                (
                    "level",
                    models.CharField(
                        choices=[
                            ("easy", "Easy"),
                            ("hard", "Hard"),
                            ("difficult", "Difficult"),
                        ],
                        default="easy",
                        max_length=30,
                    ),
                ),
                ("timer", models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="Option",
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
                ("option", models.CharField(max_length=200)),
                ("is_correct", models.BooleanField(default=False)),
                (
                    "question",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="options",
                        to="assessments.question",
                    ),
                ),
            ],
        ),
    ]