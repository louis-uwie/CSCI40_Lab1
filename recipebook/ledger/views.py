from django.shortcuts import render
from .models import Ingredient, RecipeIngredient, Recipe

def recipe_list(request):
    recipes = Recipe.objects.all()
    return render(request, 'recipeList.html', {'recipes':recipes})