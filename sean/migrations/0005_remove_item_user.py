# Generated by Django 4.2.4 on 2023-10-02 13:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sean', '0004_alter_item_role'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='user',
        ),
    ]
