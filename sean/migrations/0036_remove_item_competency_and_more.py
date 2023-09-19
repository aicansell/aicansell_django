# Generated by Django 4.2.4 on 2023-09-19 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('competency', '0001_initial'),
        ('sean', '0035_rename_competency_negativewords_competencys_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='competency',
        ),
        migrations.AlterField(
            model_name='item',
            name='competency_weak_words',
            field=models.ManyToManyField(blank=True, limit_choices_to={'competency': True}, to='sean.negativewords'),
        ),
        migrations.RemoveField(
            model_name='item',
            name='sub_competency',
        ),
        migrations.AddField(
            model_name='item',
            name='competency',
            field=models.ManyToManyField(blank=True, to='competency.competency'),
        ),
        migrations.AddField(
            model_name='item',
            name='sub_competency',
            field=models.ManyToManyField(blank=True, to='competency.sub_competency'),
        ),
    ]
