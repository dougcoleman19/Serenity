# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-12-06 15:38
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Perps',
            fields=[
                ('perp_id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(default=None, max_length=200)),
                ('middle_init', models.CharField(blank=True, default=None, max_length=1, null=True)),
                ('last_name', models.CharField(default=None, max_length=200)),
                ('birthdate', models.DateField(default=None)),
                ('date_created', models.DateField(default=datetime.date(2017, 12, 6))),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('status_id', models.AutoField(primary_key=True, serialize=False)),
                ('status_description', models.CharField(default=None, max_length=200)),
                ('date_created', models.DateField(default=datetime.date(2017, 12, 6))),
            ],
        ),
        migrations.AddField(
            model_name='perps',
            name='status_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='neighborhoodwatch.Status'),
        ),
    ]