from django.db import models
from django.contrib.auth.models import User


class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField()
    date = models.DateField(auto_now_add=True)
    review = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.User.username