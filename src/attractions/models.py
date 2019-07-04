from django.db import models


class Attractions(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    open = models.BooleanField()

    def __str__(self):
        return self.name