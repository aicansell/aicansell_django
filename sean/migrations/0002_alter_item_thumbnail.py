# Generated by Django 4.2.4 on 2023-09-04 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sean', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='thumbnail',
            field=models.ImageField(upload_to='media'),
        ),
    ]
