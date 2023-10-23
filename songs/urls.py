from django.urls import path
from . import views


urlpatterns = [
    path("albums/<int:pk>/songs/", views.SongView.as_view()),
    path("albums/<int:pk>/songs/<int:song_id>", views.SongDetailView.as_view()),
]
