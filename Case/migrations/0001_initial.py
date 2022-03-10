# Generated by Django 4.0.3 on 2022-03-09 20:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='OrderBookHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('maxFiled', models.FloatField(blank=True, max_length=1000)),
                ('minFiled', models.FloatField(blank=True, max_length=1000)),
                ('average', models.FloatField(blank=True, max_length=1000)),
                ('total', models.FloatField(blank=True, max_length=1000)),
                ('date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
        ),
    ]