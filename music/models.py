from django.db import models
from django.core.urlresolvers import reverse

# Define Artist, Album, Track, and Genre data models.

class Artist(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField(max_length=200)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('music:artist_detail', kwargs={'pk': self.pk})


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

    def get_absolute_url(self):
        return reverse('music:album_detail', kwargs={'pk': self.pk})


class Track(models.Model):
    name = models.CharField(max_length=20)
    album = models.ForeignKey('Album')

    def __str__(self):
        return self.name



