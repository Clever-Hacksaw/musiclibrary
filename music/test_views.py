from django.test import TestCase

# Uncomment when models ready to test.
# from .models import Artist, Album, Track, Genre

"""
class TestModels(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.artists = {
            "beatles": Artist.objects.create(name="Beatles"),
        }

        cls.albums = [
            Album.objects.create(title="Sgt. Peppers"),
        ]

    def test_number_of_artists(self):
        self.assertEqual(len(self.artists), Artist.objects.all().count())

    def test_get_artist_by_pk(self):
        artist = artist.objects.get(pk=self.artist["beatles"].pk)
        self.assertEqual(self.artist["beatles"], artist)

    def test_get_artist_by_name(self):
        artist = Artist.objects.get(name="Beatles")
        self.assertEqual(self.artists["beatles"], author)

    def test_update_artist(self):
        artist = Artist.objects.get(name="Beatles")
        artist.name = "Saved Beatles in test"
        artist.save()

        artist_to_check = Artist.objects.get(pk=self.artist["beatles"].pk)

        self.assertEqual(artist_to_check.name, "Saved Beatles in test")

    def test_does_not_exist_error(self):
        self.assertRaises(Artist.DoesNotExist, lambda: Artist.objects.get(name="doesnotexist"))

    def test_get_album_artists(self):
        artists = Album.objects.get(name="Sgt. Peppers").artists

        self.assertEqual(artists.count(), 1)
        self.assertEqual(list(artists.all()), [self.artists["beatles"]])
        
        """


        """
        EXAMPLE from Matt in bookworm project - for adding multiple authors to book.
        
         cls.books[3].authors.add(cls.authors["matt"], cls.authors["drew"], cls.authors["nick"])
         cls.books[4].authors.add(cls.authors["thomas"], cls.authors["travis"])

        self.assertEqual(authors.count(), 3)
        self.assertEqual(list(authors.all()), [
            self.authors["matt"],
            self.authors["drew"],
            self.authors["nick"],
        ])
        """