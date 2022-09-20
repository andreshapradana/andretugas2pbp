from django.db import models

class MyWatchList(models.Model):
    watched = models.CharField(max_length=3)
    title = models.CharField(max_length=50)
    rating = models.FloatField()
    release_date = models.TextField()
    review = models.TextField()