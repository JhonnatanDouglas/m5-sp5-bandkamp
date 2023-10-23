from django.urls import path
from . import views


urlpatterns = [
    path("albums/", views.AlbumView.as_view()),
    path("albums/<int:pk>/", views.AlbumDetailView.as_view()),
]
