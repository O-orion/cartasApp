# Generated by Django 3.2.8 on 2021-12-03 14:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Carta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=255)),
                ('tema', models.CharField(max_length=200)),
                ('remetente', models.CharField(max_length=200)),
                ('destinatario', models.CharField(max_length=200)),
                ('texto', models.TextField()),
                ('data_carta', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
        ),
    ]