from django.contrib import admin

# Import the music app models.
from .models import Artist, Album, Track, Genre

class ArtistAdmin(admin.ModelAdmin):
    search_fields = ('name', )


class AlbumAdmin(admin.ModelAdmin):
    search_fields = ('name', 'genre', 'track')
    list_display = ('name', 'get_genre', 'get_artist')

    def get_artist(self, obj):
        artists = [artist.name for artist in obj.artist.all()]
        return ", ".join(artists)

        
    def get_genre(self, obj):
        genres = [genre.name for genre in obj.genre.all()]
        return ", ".join(genres)


    get_artist.short_description = 'Artist'
    get_genre.short_description = 'Genre'


admin.site.register(Artist, ArtistAdmin)
admin.site.register(Album, AlbumAdmin)
admin.site.register(Track)
admin.site.register(Genre)
