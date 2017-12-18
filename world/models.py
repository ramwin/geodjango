# from django.db import models

# Create your models here.
from django.contrib.gis.db import models


class MyPoint3(models.Model):
    point = models.PointField(srid=4326)

    def __str__(self):
        return self.point.geojson
