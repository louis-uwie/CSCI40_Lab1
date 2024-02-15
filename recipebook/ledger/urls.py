# <appname>/urls.py
from django.urls import path
from . import views


urlpatterns = [
    path('recipe/list/', views.recipe_list, name="recipe_list"),

    ]