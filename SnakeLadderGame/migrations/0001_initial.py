# Generated by Django 5.0.2 on 2024-04-21 13:30

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("competency", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Questions",
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
                ("question", models.TextField()),
                (
                    "thumbnail",
                    models.FileField(
                        blank=True,
                        null=True,
                        upload_to="media/question/snakeladdergame/question",
                    ),
                ),
                ("timer", models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name="Options",
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
                ("option", models.CharField(max_length=300)),
                ("point", models.IntegerField(default=0)),
                (
                    "question",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="SnakeLadderGame.questions",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="SnakeLadderGame",
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
                ("name", models.CharField(max_length=100)),
                ("description", models.TextField()),
                (
                    "thumbnail",
                    models.FileField(
                        blank=True,
                        null=True,
                        upload_to="media/game/snakeladdergame/thumbnail",
                    ),
                ),
                (
                    "competency",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="competency.competency",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="questions",
            name="snakeladdergame",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="SnakeLadderGame.snakeladdergame",
            ),
        ),
        migrations.CreateModel(
            name="SnakeLadderGameResult",
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
                ("score", models.IntegerField(default=0)),
                ("created_at", models.DateField(auto_now_add=True)),
                (
                    "snakeladdergame",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="SnakeLadderGame.snakeladdergame",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "unique_together": {("snakeladdergame", "user")},
            },
        ),
    ]
