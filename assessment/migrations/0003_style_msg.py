# Generated by Django 4.2.4 on 2024-02-03 20:10

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("assessment", "0002_alter_situation_name"),
    ]

    operations = [
        migrations.AddField(
            model_name="style",
            name="msg",
            field=models.TextField(blank=True, null=True),
        ),
    ]
