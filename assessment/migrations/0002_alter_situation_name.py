# Generated by Django 4.2.4 on 2024-02-03 15:33

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("assessment", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="situation",
            name="name",
            field=models.CharField(max_length=500),
        ),
    ]
