from django.db import models

# Define Artist, Album, Track, and Genre data models.

class Artist():
    name = models.CharField(max_length=20)
    description = models.TextField()

    def __str__(self):
        return self.name


class Album():
    name = models.CharField(max_length=20)
    artist = models.ManyToManyField('Artist')
    genre = models.ManyToManyField('Genre')
    description = models.TextField()

    def __str__(self):
        return self.name
    

class Track():
    name = models.CharField(max_length=20)
    album = models.ForeignKey('Album')

    def __str__(self):
        return self.name


class Genre():
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name
