from django.shortcuts import get_object_or_404

from rest_framework import status
from rest_framework.response import Response

from recipes.models import Recipe
from api.serializers.recipes_serializers import FavoriteSerializer


def delete(request, id, model):
    user = request.user
    recipe = get_object_or_404(Recipe, id=id)
    if not model.objects.filter(user=user, recipe=recipe).exists():
        return Response(
            {
                "errors": "Remove from 'shopping list/favorites' not available"
            },
            status=status.HTTP_400_BAD_REQUEST,
        )
    obj = get_object_or_404(model, user=user, recipe=recipe)
    obj.delete()
    return Response(
        {"errors": "Recipe removed successfully from 'shopping list/favorites'."},
        status=status.HTTP_204_NO_CONTENT,
    )


def post(request, id, model):
    user = request.user
    recipe = get_object_or_404(Recipe, id=id)
    if model.objects.filter(user=user, recipe=recipe).exists():
        return Response(
            {
                "errors": "Attaching to 'shopping list/favorites' not available"
            },
            status=status.HTTP_400_BAD_REQUEST,
        )
    model.objects.get_or_create(user=user, recipe=recipe)
    serializer = FavoriteSerializer(recipe, context={"request": request})
    return Response(serializer.data, status=status.HTTP_201_CREATED)
