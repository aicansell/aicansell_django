# Generated by Django 4.2.4 on 2023-09-20 07:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sean', '0041_traits'),
    ]

    operations = [
        migrations.AddField(
            model_name='traits',
            name='trait_name',
            field=models.CharField(blank=True, max_length=250),
        ),
    ]
