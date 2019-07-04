from django.db import models
from tourist_attraction.models import TouristAttraction
from comments.models import Comment
from reviews.models import Review
from location.models import Location


class Attractions(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    open = models.BooleanField()
    tourist_attractions = models.ManyToManyField(TouristAttraction)
    review = models.ManyToManyField(Review)
    comments = models.ManyToManyField(Comment)
    location = models.ForeignKey(Location, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name