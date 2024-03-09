# Generated by Django 5.0.2 on 2024-03-08 16:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("assessments", "0002_assessment_assessmentresult_assessmenttype_and_more"),
        ("learningcourse", "0001_initial"),
        ("orgss", "0001_initial"),
        ("sean", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name='Seasons',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('description', models.TextField(blank=True, null=True)),
                ('thumbnail', models.FileField(blank=True, null=True, upload_to='media/series/seasons/thumbnail')),
            ],
        ),
        migrations.CreateModel(
            name='LearningCourseSeason',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('learning_course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='learningcourse.learningcourse')),
                ('season', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='series.seasons')),
            ],
        ),
        migrations.CreateModel(
            name='ItemSeason',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sean.item')),
                ('season', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='series.seasons')),
            ],
        ),
        migrations.CreateModel(
            name='AssessmentSeason',
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
                    "assessment",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="assessments.assessmenttype",
                    ),
                ),
                (
                    "season",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="series.seasons"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name='Series',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('description', models.TextField(blank=True, null=True)),
                ('thumbnail', models.FileField(blank=True, null=True, upload_to='media/series/thumbnail')),
                ('sub_org', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orgss.suborg')),
            ],
        ),
        migrations.AddField(
            model_name='seasons',
            name='series',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='series.series'),
        ),
    ]
