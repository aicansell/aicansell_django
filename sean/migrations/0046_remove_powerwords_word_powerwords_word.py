# Generated by Django 4.2.4 on 2023-09-20 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('words', '0001_initial'),
        ('sean', '0045_alter_traits_trait_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='powerwords',
            name='word',
        ),
        migrations.AddField(
            model_name='powerwords',
            name='word',
            field=models.ManyToManyField(to='words.words'),
        ),
    ]
