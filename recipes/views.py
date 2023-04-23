from django.db.models import Count
from rest_framework import generics, permissions, filters
from feedme_api.permissions import IsOwnerOrReadOnly
from .models import Recipe
from .serializers import RecipeSerializer


class RecipeList(generics.ListCreateAPIView):
    """
    List recipes or create a recipe if logged in
    The perform_create method associates the recipe with the logged in user.
    """
    serializer_class = RecipeSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Recipe.objects.annotate(
        likes_count=Count('likes', distinct=True),
        comments_count=Count('comment', distinct=True)
    ).order_by('-created_at')

    filter_backends = [
        filters.OrderingFilter,
    ]
    ordering_fields = [
        'likes_count',
        'comments_count',
    ]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class RecipeDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve a recipe and update or delete it if you own it.
    """
    serializer_class = RecipeSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Recipe.objects.annotate(
        likes_count=Count('likes', distinct=True),
        comments_count=Count('comment', distinct=True)
    ).order_by('-created_at')
