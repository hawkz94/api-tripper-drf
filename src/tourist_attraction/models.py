from django.db import models

# Create your models here.

class TouristAttraction(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    work_hour = models.TextField()
    minimun_age = models.IntegerField()

    def __str__(self):
        return self.name
