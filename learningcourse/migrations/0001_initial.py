# Generated by Django 5.0.2 on 2024-03-07 17:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("orgss", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="LearningCourse",
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
                ("name", models.CharField(max_length=300)),
                ("description", models.TextField(blank=True, null=True)),
                (
                    "thumbnail",
                    models.FileField(
                        blank=True,
                        null=True,
                        upload_to="media/learningcourse/thumbnail",
                    ),
                ),
                (
                    "sub_org",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="orgss.suborg"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="LearningCourseDocument",
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
                (
                    "document",
                    models.FileField(upload_to="media/learningcourse/document"),
                ),
                (
                    "course",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="learningcourse.learningcourse",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="LearningCourseVideo",
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
                ("video", models.FileField(upload_to="media/learningcourse/video")),
                (
                    "course",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="learningcourse.learningcourse",
                    ),
                ),
            ],
        ),
    ]
