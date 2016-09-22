from django.shortcuts import render, get_object_or_404
from django.db.models import Count
from django.core.urlresolvers import reverse
# NOTE: Remove any above we don't use.

# Import the music app models.
from .models import Artist, Album, Track, Genre

def index(request):
    return render(request, "music/index.html")

# Artist data views.

def artist_list():
    pass

def artist_detail():
    pass

# Album data views.

def album_list():
    pass

def album_detail():
    pass

# Track data views.

def track_list():
    pass

def track_detail():
    pass

# Genre data views.

def genre_list():
    pass

def genre_detail():
    pass


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
