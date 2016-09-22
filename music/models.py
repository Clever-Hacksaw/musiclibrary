from django.db import models

# Define Artist, Album, Track, and Genre data models.

class Artist(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField(max_length=200)

    def __str__(self):
        return self.name

class Genre(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Album(models.Model):
    name = models.CharField(max_length=20)
    artist = models.ManyToManyField('Artist')
    genre = models.ManyToManyField('Genre')
    description = models.TextField(max_length=200)

    def __str__(self):
        return self.name
    

class Track(models.Model):
    name = models.CharField(max_length=20)
    album = models.ForeignKey('Album')

    def __str__(self):
        return self.name



