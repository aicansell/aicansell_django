# Generated by Django 4.2.4 on 2023-11-23 09:20

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("sean", "0006_alter_item_user_powerwords_alter_item_user_weakwords"),
    ]

    operations = [
        migrations.AlterField(
            model_name="item",
            name="item_answer",
            field=models.TextField(default="Your answer"),
        ),
        migrations.AlterField(
            model_name="item",
            name="user_powerwords",
            field=models.TextField(default=""),
        ),
        migrations.AlterField(
            model_name="item",
            name="user_weakwords",
            field=models.TextField(default=""),
        ),
    ]
