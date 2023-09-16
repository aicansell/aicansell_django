# Generated by Django 4.2.4 on 2023-09-13 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sean', '0019_item_level'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='item_type',
            field=models.CharField(choices=[('Simulation', 'Simulation'), ('Email', 'Email')], default='Simulation', max_length=16),
        ),
        migrations.AddField(
            model_name='item',
            name='negative_traits',
            field=models.CharField(default='nt', max_length=300),
        ),
        migrations.AddField(
            model_name='item',
            name='positive_traits',
            field=models.CharField(default='pt', max_length=300),
        ),
        migrations.AddField(
            model_name='item',
            name='user_powerwords',
            field=models.CharField(default='up', max_length=300),
        ),
        migrations.AddField(
            model_name='item',
            name='user_weakwords',
            field=models.CharField(default='unp', max_length=300),
        ),
    ]