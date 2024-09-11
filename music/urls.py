from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ArtistViewSet, AlbumViewSet, PlaylistViewSet, SongViewSet

router = DefaultRouter()
router.register(r'artists', ArtistViewSet)
router.register(r'albums', AlbumViewSet)
router.register(r'playlists', PlaylistViewSet)
router.register(r'songs', SongViewSet)

urlpatterns = [
    path('', include(router.urls)),
]