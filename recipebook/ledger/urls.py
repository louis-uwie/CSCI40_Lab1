from django.urls import path
from django.contrib.auth.decorators import login_required
from . import views

urlpatterns = [
    path('recipes/list/', login_required(views.RecipeListView.as_view()), name='recipe_list'),
    path('recipes/<int:pk>/', login_required(views.RecipeDetailView.as_view()), name='recipe_detail'),
    path('login/', views.login_view, name='login'), 
    path('logout/', views.logout_view, name='logout'), 
]
