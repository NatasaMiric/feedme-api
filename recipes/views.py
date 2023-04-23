from rest_framework import status, permissions
from .models import Recipe
from .serializers import RecipeSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import Http404
from feedme_api.permissions import IsOwnerOrReadOnly


class RecipeList(APIView):
    """
    List all Recipes and create a recipe as logged in user,
    recipe related to User instance
    """
    serializer_class = RecipeSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request):
        recipes = Recipe.objects.all()
        serializer = RecipeSerializer(
            recipes, many=True, context={'request': request}
        )
        return Response(serializer.data)

    def post(self, request):
        serializer = RecipeSerializer(
            data=request.data, context={'request': request}
        )
        if serializer.is_valid():
            serializer.save(owner=request.user)
            return Response(
                serializer.data, status=status.HTTP_201_CREATED
            )
        return Response(
            serializer.errors, status=status.HTTP_400_BAD_REQUEST
        )


class RecipeDetail(APIView):
    """
    Recipe Detail View to retrieve a recipe, and update a recipe
    and delete a recipe if you own it
    """

    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = RecipeSerializer

    def get_object(self, pk):
        try:
            recipe = Recipe.objects.get(pk=pk)
            self.check_object_permissions(self.request, recipe)
            return recipe
        except Recipe.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        recipe = self.get_object(pk)
        serializer = RecipeSerializer(
            recipe, context={'request': request}
        )
        return Response(serializer.data)

    def put(self, request, pk):
        recipe = self.get_object(pk)
        serializer = RecipeSerializer(
            recipe, data=request.data, context={'request': request}
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(
            serializer.errors, status=status.HTTP_400_BAD_REQUEST
        )

    def delete(self, request, pk):
        recipe = self.get_object(pk)
        recipe.delete()
        return Response(
            status=status.HTTP_204_NO_CONTENT
        )
