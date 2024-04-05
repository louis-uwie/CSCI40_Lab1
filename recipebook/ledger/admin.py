from django.contrib import admin

from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import Profile, Recipe, RecipeImage, RecipeIngredient, Ingredient

class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'Profile'



class RecipeInline(admin.TabularInline):
    model = RecipeIngredient
    can_delete = True
    verbose_name_plural = 'Recipes'



class RecipeAdmin(admin.ModelAdmin):
    inlines = [RecipeInline]



class CustomUserAdmin(UserAdmin):
    inlines = [ProfileInline]



admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
admin.site.register(Recipe, RecipeAdmin)

