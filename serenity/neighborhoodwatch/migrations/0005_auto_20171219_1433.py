# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-12-19 20:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('neighborhoodwatch', '0004_auto_20171219_0856'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='perps',
            name='created_by',
        ),
        migrations.AlterField(
            model_name='perps',
            name='birthdate',
            field=models.CharField(blank=True, default=None, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='perps',
            name='date_created',
            field=models.CharField(blank=True, default=None, max_length=15, null=True),
        ),
    ]
