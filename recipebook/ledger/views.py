from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.shortcuts import render, redirect
from django.contrib.auth import logout, login, authenticate
from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Recipe
from .forms import RecipeImageForm
from .forms import RecipeForm


'''
Logging in and out of the site.
'''
def password_reset_confirm():
    pass


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('recipe_list')
        
        else:
            messages.error(request, 'Invalid username or password.')

    return render(request, 'registration/login.html')


def logout_view(request):
    logout(request)
    # Redirect to a success page or homepage
    return redirect('login')


'''
Method for uploading a new recipe.
'''
def upload_recipe(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST)
        
        if form.is_valid():
            recipe = Recipe(name=form.cleaned_data['name'], author=request.user)
            recipe.save()
            print("Recipe saved successfully:", recipe)
            return redirect('recipe_list')
        
    else:
        
        form = RecipeForm()
        
    return render(request, 'recipe_create.html', {'form': form})


'''
Method for uploading images to the recipe.
'''
def upload_image(request):
    if request.method == 'POST':
        form = RecipeImageForm(request.POST, request.FILES)
        if form.is_valid():
            print("Form is valid")  # Debug statement
            recipe_image = form.save(commit=False)
            recipe_image.author = request.user
            recipe_image.save()
            print("Recipe image saved:", recipe_image)  # Debug statement
            return redirect('success_url')
        else:
            print("Form errors:", form.errors)  # Debug statement
    else:
        form = RecipeImageForm()
    return render(request, 'recipe_create.html', {'form': form})


'''
View for the recipe list page.
'''
class RecipeListView(LoginRequiredMixin, ListView):

    model = Recipe
    template_name = 'recipeList.html'
    context_object_name = 'recipes'
    

'''
View for the recipe details page.
'''
class RecipeDetailView(LoginRequiredMixin, DetailView):

    model = Recipe
    template_name = 'recipeDetails.html'
    context_object_name = 'recipe'