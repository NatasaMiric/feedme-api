from rest_framework import generics, permissions
from feedme_api.permissions import IsOwnerOrReadOnly
from .models import Bookmark
from .serializers import BookmarkSerializer


class BookmarkList(generics.ListCreateAPIView):
    """
    List all bookmarks for the currently authenticated user.
    Create a bookmark if authenticated.
    The perform_create method associates the bookmark with the logged in user.
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = BookmarkSerializer

    def get_queryset(self):
        user = self.request.user
        queryset = Bookmark.objects.filter(
            owner=user.id).order_by('-created_at')
        return queryset

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class BookmarkDetail(generics.RetrieveDestroyAPIView):
    """
    Retrieve a bookmark. No Update view,
    as users can only save or unsave a recipe.
    Destroy a bookmark, i.e. unsave a post if owner of that save.
    """
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = BookmarkSerializer

    def get_queryset(self):
        user = self.request.user
        queryset = Bookmark.objects.filter(owner=user)
        return queryset
