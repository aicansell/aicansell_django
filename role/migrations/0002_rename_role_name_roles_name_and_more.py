# Generated by Django 4.2.4 on 2023-10-14 07:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('role', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='roles',
            old_name='role_name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='sub_role',
            old_name='sub_role',
            new_name='role',
        ),
        migrations.RenameField(
            model_name='sub_role',
            old_name='subrole_name',
            new_name='subrole',
        ),
    ]
