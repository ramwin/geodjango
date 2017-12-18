#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang @ 2017-12-12 11:35:01


from django.core.management.base import BaseCommand
import json
from world.models import MyPoint3
from django.contrib.gis.geos import Point
from django.contrib.gis.geos import GEOSGeometry


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        point = Point(0,0)
        MyPoint3.objects.create(point=point)
        print(MyPoint3.objects.filter(point__distance_lte=(point, 1)))
