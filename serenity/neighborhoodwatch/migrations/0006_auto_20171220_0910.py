# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-12-20 15:10
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('neighborhoodwatch', '0005_auto_20171219_1433'),
    ]

    operations = [
        migrations.AlterField(
            model_name='status',
            name='date_created',
            field=models.DateField(default=datetime.date(2017, 12, 20)),
        ),
    ]
