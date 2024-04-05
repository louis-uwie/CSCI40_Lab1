from django.contrib import admin

from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import Profile, Recipe, RecipeImage

class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'Profile'

class CustomUserAdmin(UserAdmin):
    inlines = (ProfileInline,)


class Recipe():
    model = Recipe
    can_delete = True
    verbose_name_plural = 'Recipes'

class RecipeAdmin():
    
    pass

admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
