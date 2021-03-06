# -*- coding: utf-8 -*-
# Generated by Django 1.9.3 on 2016-03-03 21:56
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Zombie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('date_of_birth', models.DateField()),
                ('date_of_rebirth', models.DateField(default=datetime.date(2016, 3, 3))),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='avatars')),
                ('bio', models.TextField()),
            ],
        ),
    ]
