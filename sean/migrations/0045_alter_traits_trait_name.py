# Generated by Django 4.2.4 on 2023-09-20 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sean', '0044_remove_powerwords_trait_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='traits',
            name='trait_name',
            field=models.CharField(default='trait', max_length=250),
        ),
    ]