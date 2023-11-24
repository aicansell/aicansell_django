# Generated by Django 4.2.4 on 2023-11-23 09:20

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("accounts", "0008_alter_userprofile_user_powerwords_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="userprofile",
            name="scenario_attempt_pw",
            field=models.TextField(default=""),
        ),
        migrations.AlterField(
            model_name="userprofile",
            name="scenario_attempt_ww",
            field=models.TextField(default=""),
        ),
        migrations.AlterField(
            model_name="userprofile",
            name="scenarios_attempted_score",
            field=models.TextField(blank=True, default="", null=True),
        ),
        migrations.AlterField(
            model_name="userprofile",
            name="user_powerwords",
            field=models.TextField(default=""),
        ),
        migrations.AlterField(
            model_name="userprofile",
            name="user_weakwords",
            field=models.TextField(default=""),
        ),
    ]
