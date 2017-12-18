#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang @ 2017-12-12 11:35:01


from django.core.management.base import BaseCommand
import json
from world.models import MyPoint, SouthTexasCity, MyPoint3, MyPoint2
from django.contrib.gis.geos import Point
from django.contrib.gis.geos import GEOSGeometry


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        point1 = Point(1,1)
        point2 = GEOSGeometry('POINT(0 0)', srid=4326)
        point3 = GEOSGeometry('POINT(-96.876369 29.905320)', srid=4326)
        try:
            print(SouthTexasCity.objects.filter(point__distance_lt=(point1,1)))
        except:
            print("point1 失败")
        try:
            print(SouthTexasCity.objects.filter(point__distance_lt=(point2,1)))
        except:
            print("point2 失败")
        try:
            print(MyPoint3.objects.filter(point__distance_lte=(point3, 7000)))
        except Exception as e:
            print(e)
            print("point3 失败")
        # print(MyPoint.objects.filter(point__distance_lt=(point,1)))
        pass
