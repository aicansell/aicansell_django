# Generated by Django 4.2.4 on 2023-09-19 09:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sean', '0036_remove_item_competency_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='competency',
            new_name='competencys',
        ),
    ]