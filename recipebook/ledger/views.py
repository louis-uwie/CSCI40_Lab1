from typing import Any
from django.shortcuts import render, get_object_or_404
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Ingredient, RecipeIngredient, Recipe

#def recipe_list(request):
#     recipes = Recipe.objects.all()
#     return render(request, 'recipeList.html', {'recipes':recipes})

class RecipeListView(ListView):

    template_name = 'recipeList.html'
    model = Recipe
    context_object_name = 'recipes'

# def recipe_detail(request, id):
#     recipe = get_object_or_404(Recipe, id=id)
#     ingredients = recipe.recipeingredient_set.all()

#     context = {'recipe': recipe, 'ingredients': ingredients}

#     return render(request, 'recipe_1.html', context)
    
class RecipeDetailView(DetailView):
    model = Recipe
    template_name = 'recipe_1.html'
    context_object_name = 'recipe'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Fetch the recipe object
        recipe = self.get_object()
        # Get the list of ingredients for the recipe
        ingredients = recipe.recipeingredient_set.all()
        # Add the ingredients to the context
        context['ingredients'] = ingredients
        return context