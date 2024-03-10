# Generated by Django 5.0.2 on 2024-03-09 16:58

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("sean", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="item",
            name="expert",
            field=models.FileField(
                blank=True, null=True, upload_to="media/item/expert"
            ),
        ),
        migrations.AlterField(
            model_name="item",
            name="negative_traits",
            field=models.CharField(blank=True, default="", max_length=300),
        ),
        migrations.AlterField(
            model_name="item",
            name="positive_traits",
            field=models.CharField(blank=True, default="", max_length=300),
        ),
    ]