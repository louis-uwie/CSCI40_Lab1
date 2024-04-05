from django.urls import path
from django.contrib.auth.decorators import login_required
from . import views

urlpatterns = [

    path('login/', views.login_view, name='login'), 
    path('logout/', views.logout_view, name='logout'), 

    path('recipes/list/', login_required(views.RecipeListView.as_view()), name='recipe_list'), #For Viewing Recipe List
    path('recipe/<int:pk>/', login_required(views.RecipeDetailView.as_view()), name='recipe_detail'), #For Viewing Specific Recipes
    
    path('recipe/add/', views.upload_recipe, name='upload_recipe'), #For Uploading Recipes
    path('recipe/add/', views.upload_image, name='upload_image'), #For Uploading Images
    
]
