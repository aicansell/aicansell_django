# Generated by Django 4.2.4 on 2023-09-20 04:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('competency', '0002_remove_sub_competency_sub_competency_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='competency',
            name='sub_competency',
            field=models.ManyToManyField(blank=True, to='competency.sub_competency'),
        ),
    ]