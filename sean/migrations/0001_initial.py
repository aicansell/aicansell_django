# Generated by Django 4.2.4 on 2023-09-27 14:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('words', '0001_initial'),
        ('competency', '0001_initial'),
        ('orgss', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Collection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('collection_name', models.CharField(default='collection', max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='EmotionWords',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emotion_word_name', models.CharField(max_length=250)),
                ('competencys', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='competency.competency')),
                ('sub_competency', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='competency.sub_competency')),
                ('word', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='words.words')),
            ],
        ),
        migrations.CreateModel(
            name='Suggestion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('suggestion_text', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Traits',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trait_name', models.CharField(default='trait', max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='PowerWords',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weight', models.IntegerField(default=1)),
                ('sentence', models.CharField(default='sentence', max_length=250)),
                ('power_word_name', models.CharField(default='pw', max_length=250)),
                ('sub_competency', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='competency.sub_competency')),
                ('word', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='words.words')),
            ],
        ),
        migrations.CreateModel(
            name='NegativeWords',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weight', models.IntegerField(default=-7)),
                ('sentence', models.CharField(default='sentence', max_length=250)),
                ('negative_word_name', models.CharField(default='ww', max_length=250)),
                ('sub_competency', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='competency.sub_competency')),
                ('word', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='words.words')),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(max_length=256)),
                ('item_description', models.CharField(blank=True, max_length=300, null=True)),
                ('item_answer', models.TextField(default='Your answer', max_length=700)),
                ('item_emotion', models.TextField(default='emotions')),
                ('item_answercount', models.IntegerField(default=1)),
                ('category', models.CharField(blank=True, default='Personal', max_length=256)),
                ('thumbnail', models.ImageField(default='c.png', upload_to='media')),
                ('item_gender', models.CharField(choices=[('Female', 'Female'), ('Male', 'Male'), ('All', 'All')], default='All', max_length=7)),
                ('item_type', models.CharField(choices=[('Simulation', 'Simulation'), ('Email', 'Email')], default='Simulation', max_length=16)),
                ('coming_across_as', models.CharField(default='sugestions', max_length=250)),
                ('level', models.IntegerField(default=1)),
                ('positive_traits', models.CharField(blank=True, default=' ', max_length=300)),
                ('negative_traits', models.CharField(blank=True, default=' ', max_length=300)),
                ('user_powerwords', models.CharField(default='up', max_length=300)),
                ('user_weakwords', models.CharField(default='unp', max_length=300)),
                ('expert', models.FileField(blank=True, null=True, upload_to='media')),
                ('competency_emotion_word', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='sean.emotionwords')),
                ('competency_power_words', models.ManyToManyField(blank=True, to='sean.powerwords')),
                ('competency_weak_words', models.ManyToManyField(blank=True, to='sean.negativewords')),
                ('competencys', models.ManyToManyField(blank=True, to='competency.competency')),
                ('role', models.ForeignKey(default=4, on_delete=django.db.models.deletion.CASCADE, to='orgss.org_roles')),
                ('sub_competency', models.ManyToManyField(blank=True, to='competency.sub_competency')),
            ],
        ),
    ]
