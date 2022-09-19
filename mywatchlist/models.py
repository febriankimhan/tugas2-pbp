from pyexpat import model
from statistics import mode
from django.db import models

# Create your models here.
class MyWatchList(models.Model):
    watched = models.BooleanField()
    title = models.TextField()
    rating = models.IntegerField()
    release_date = models.DateField()
    review = models.TextField()