# Generated by Django 4.2.4 on 2023-09-08 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sean', '0013_item_competency_item_sub_competency'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='improvement',
            field=models.CharField(default='improve on', max_length=300),
        ),
    ]