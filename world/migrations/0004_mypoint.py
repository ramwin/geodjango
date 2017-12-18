# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-18 07:01
from __future__ import unicode_literals

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('world', '0003_auto_20171218_0658'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyPoint',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('point', django.contrib.gis.db.models.fields.PointField(srid=4326)),
            ],
        ),
    ]
