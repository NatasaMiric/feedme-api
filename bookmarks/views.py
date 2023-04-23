from rest_framework import generics, permissions
from feedme_api.permissions import IsOwnerOrReadOnly
from .models import Bookmark
from .serializers import BookmarkSerializer


class BookmarkList(generics.ListCreateAPIView):
    """
    List all bookmarks. Create a bookmark if authenticated.
    The perform_create method associates the bookmark with the logged in user.
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = BookmarkSerializer
    queryset = Bookmark.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class BookmarkDetail(generics.RetrieveDestroyAPIView):
    """
    Retrieve a like. No Update view, as users can only save or unsave a recipe.
    Destroy a like, i.e. unsave a post if owner of that save.
    """
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Bookmark.objects.all()
    serializer_class = BookmarkSerializer
