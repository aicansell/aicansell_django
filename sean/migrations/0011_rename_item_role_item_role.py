# Generated by Django 4.2.4 on 2023-09-06 14:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sean', '0010_item_suggestions'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='item_role',
            new_name='role',
        ),
    ]