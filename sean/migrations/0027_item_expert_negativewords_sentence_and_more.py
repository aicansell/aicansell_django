# Generated by Django 4.2.4 on 2023-09-19 05:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sean', '0026_emotionwords_word'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='expert',
            field=models.FileField(blank=True, null=True, upload_to='media'),
        ),
        migrations.AddField(
            model_name='negativewords',
            name='sentence',
            field=models.CharField(default='sentence', max_length=250),
        ),
        migrations.AddField(
            model_name='powerwords',
            name='sentence',
            field=models.CharField(default='sentence', max_length=250),
        ),
    ]
