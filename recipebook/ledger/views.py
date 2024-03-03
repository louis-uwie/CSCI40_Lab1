from django.shortcuts import render
from .models import Recipe  # Import the Recipe model

def recipe_list(request):
    # Fetch all recipes from the database
    recipes = Recipe.objects.all()

    ctx = {
        "recipes": recipes
    }

    return render(request, "recipeList.html", ctx)
