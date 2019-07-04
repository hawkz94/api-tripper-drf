from django.db import models

class Location(models.Model):
    linha1 = models.CharField(max_length=150)
    linha2 = models.CharField(max_length=150, null=True, blank=True)
    estado = models.CharField(max_length=2)
    cidade = models.CharField(max_length=150)
    lat = models.IntegerField(null=True, blank=True)
    lng = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.linha1
