# Generated by Django 4.2.4 on 2023-09-13 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sean', '0022_alter_item_negative_traits_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='negativewords',
            name='weight',
            field=models.IntegerField(default=-7),
        ),
        migrations.AddField(
            model_name='powerwords',
            name='weight',
            field=models.IntegerField(default=1),
        ),
    ]