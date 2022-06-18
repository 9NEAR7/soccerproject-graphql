from django.db import models

# Create your models here.
class Player(models.Model):
    name = models.TextField()
    nationality = models.TextField()
    date = models.TextField()
    team = models.TextField(blank=True)
    url = models.URLField()


