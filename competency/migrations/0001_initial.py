# Generated by Django 4.2.4 on 2024-02-26 16:28

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("words", "__first__"),
    ]

    operations = [
        migrations.CreateModel(
            name="Competency",
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
                ("competency_name", models.CharField(max_length=250, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name="Senti",
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
                ("name", models.CharField(max_length=250, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name="Sub_Competency",
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
                ("name", models.CharField(max_length=250, unique=True)),
                (
                    "emotion_words",
                    models.ManyToManyField(blank=True, to="words.emotionwords"),
                ),
                (
                    "negative_words",
                    models.ManyToManyField(blank=True, to="words.negativewords"),
                ),
                (
                    "power_words",
                    models.ManyToManyField(blank=True, to="words.powerwords"),
                ),
            ],
        ),
        migrations.CreateModel(
            name="MasterCompetency",
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
                ("name", models.CharField(max_length=250, unique=True)),
                (
                    "master_competency",
                    models.ManyToManyField(blank=True, to="competency.competency"),
                ),
            ],
        ),
        migrations.AddField(
            model_name="competency",
            name="competency_sentiment",
            field=models.ManyToManyField(blank=True, to="competency.senti"),
        ),
        migrations.AddField(
            model_name="competency",
            name="sub_competency",
            field=models.ManyToManyField(blank=True, to="competency.sub_competency"),
        ),
    ]
