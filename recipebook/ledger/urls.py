# <appname>/urls.py
from django.urls import path
from . import views


urlpatterns = [

    path('recipes/list/', views.RecipeListView.as_view(), name="recipe_list"),
    path('recipes/<int:pk>/', views.RecipeDetailView.as_view(), name="recipe_detail"),

    ]