from django.shortcuts import render, get_object_or_404
from .models import Ingredient, RecipeIngredient, Recipe

def recipe_list(request):
    recipes = Recipe.objects.all()
    return render(request, 'recipeList.html', {'recipes':recipes})

def recipe_detail(request, id):
    recipe = get_object_or_404(Recipe, id=id)
    ingredients = recipe.recipeingredient_set.all()
    context = {'recipe': recipe, 'ingredients': ingredients}
    return render(request, 'recipe_1.html', context)




