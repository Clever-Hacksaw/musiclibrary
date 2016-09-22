from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name="index"),

    url(r'^artist-list/$', views.ArtistList.as_view(), name="artist_list"),
    url(r'^(?P<pk>\d+)/artist-detail/$', views.ArtistDetail.as_view(), name="artist_detail"),

    url(r'^album-list/$', views.AlbumList.as_view(), name="album_list"),
    url(r'^(?P<pk>\d+)/album-detail/$', views.AlbumDetail.as_view(), name="album_detail"),

    url(r'^track-list/$', views.TrackList.as_view(), name="track_list"),
    url(r'^(?P<pk>\d+)/track-detail/$', views.TrackDetail.as_view(), name="track_detail"),

    url(r'^genre-list/$', views.AlbumList.as_view(), name="genre_list"),
    url(r'^(?P<pk>\d+)/genre-detail/$', views.GenreDetail.as_view(), name="genre_detail"),
]

