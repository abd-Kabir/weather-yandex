from django.db import models


class City(models.Model):
    name = models.CharField(max_length=100)
    lat = models.CharField(max_length=100)
    lon = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.name} (lat: {self.lat}, lon: {self.lon})'

    class Meta:
        db_table = 'City'
