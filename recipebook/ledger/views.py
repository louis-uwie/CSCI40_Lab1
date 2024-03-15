from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.shortcuts import render, redirect
from django.contrib.auth import logout, login, authenticate
from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Recipe

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



class RecipeListView(LoginRequiredMixin, ListView):

    template_name = 'recipeList.html'
    model = Recipe
    context_object_name = 'recipes'
    


class RecipeDetailView(LoginRequiredMixin, DetailView):

    model = Recipe
    template_name = 'recipeDetails.html'
    context_object_name = 'recipe'