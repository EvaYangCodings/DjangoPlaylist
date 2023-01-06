from django.db import models

# Create your models here.
class Song(models.Model):
    track = models.CharField(max_length=50)
    artist = models.CharField(max_length=50, unique= True)
    album = models.CharField(max_length=70)
    length = models.TimeField()

class Playlist(models.Model):
    name = models.CharField(max_length=70, unique= True)
    number_of_songs=models.IntegerField()