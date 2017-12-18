# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-18 06:58
from __future__ import unicode_literals

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('world', '0002_auto_20171218_0635'),
    ]

    operations = [
        migrations.CreateModel(
            name='SouthTexasCity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('point', django.contrib.gis.db.models.fields.PointField(srid=32140)),
            ],
        ),
        migrations.DeleteModel(
            name='Point',
        ),
    ]