# Generated by Django 4.2.4 on 2023-09-21 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sean', '0048_alter_item_competency_power_words_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Collection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('collection_name', models.CharField(default='collection', max_length=250)),
            ],
        ),
    ]
