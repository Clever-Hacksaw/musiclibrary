from django.shortcuts import render, get_object_or_404
from django.db.models import Count
from django.core.urlresolvers import reverse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
# NOTE: Remove any above we don't use.

# Import the music app models.
from .models import Artist, Album, Track, Genre

def index(request):
    return render(request, "music/index.html")

# Artist data views.

class ArtistList(ListView):
    model = Artist

class ArtistDetail(DetailView):
    model = Artist

class ArtistCreate(CreateView):
    model = Artist
    fields = ('name', 'description', )
    template_name = "music/index.html"

# Album data views.

class AlbumList(ListView):
    model = Album

class AlbumDetail(DetailView):
    model = Album

# Track data views.

class TrackList(ListView):
    model = Track

class TrackDetail(DetailView):
    model = Track

# Genre data views.

class GenreList(ListView):
    model = Genre

class GenreDetail(DetailView):
    model = Genre


# Reference from bookworm.

"""
def bookcase_list(request):
    bookcases = Bookcase.objects.annotate(shelf_count=Count('bookshelf')).all()

    breadcrumbs = (
        ("Bookcases", ),
    )

    context = {
        "bookcases": bookcases,
        "breadcrumbs": breadcrumbs,
    }
    return render(request, "bookcases/bookcase_list.html", context)

def bookcase_detail(request, id):
    bookcase = get_object_or_404(Bookcase, pk=id)
    bookshelves = bookcase.bookshelf_set.annotate(book_count=Count('book')).all()

    breadcrumbs = (
        ("Bookcases", reverse("bookcases:bookcase_list")),
        (bookcase.name, )
    )

    context = {
        "bookcase": bookcase,
        "bookshelves": bookshelves,
        "breadcrumbs": breadcrumbs,
    }

    return render(request, "bookcases/bookcase_detail.html", context)
"""
