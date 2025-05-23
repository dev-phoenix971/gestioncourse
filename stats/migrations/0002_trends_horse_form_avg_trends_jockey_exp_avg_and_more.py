# Generated by Django 5.1.6 on 2025-02-26 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stats', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='trends',
            name='horse_form_avg',
            field=models.FloatField(default=0.5),
        ),
        migrations.AddField(
            model_name='trends',
            name='jockey_exp_avg',
            field=models.FloatField(default=0.5),
        ),
        migrations.AddField(
            model_name='trends',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='trends',
            name='weather_avg',
            field=models.FloatField(default=0.5),
        ),
    ]
