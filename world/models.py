# from django.db import models

# Create your models here.
from django.contrib.gis.db import models


# class Point(models.Model):
#     point = models.PointField()


class SouthTexasCity(models.Model):
    name = models.CharField(max_length=30)
    point = models.PointField(srid=32140)


class MyPoint3(models.Model):
    point = models.PointField(srid=4326)

    def __str__(self):
        return self.point.geojson
