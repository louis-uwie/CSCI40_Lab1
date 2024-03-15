from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

def minimumBio(a):
    if a < 255: raise ValidationError("Bio should be at least 255 characters.")

'''
Test Users:
    username: Tyrone
    password: usertest1
'''
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.TextField(max_length=50, blank=True)
    user_bio = models.TextField(max_length=756, validators=[minimumBio])

    def __str__(self):
        return self.name

class Recipe(models.Model):
    name = models.CharField(max_length=100)
    author = models.ForeignKey(Profile, on_delete=models.CASCADE, default=None, null=True)

    def __str__(self):
        return self.name
    


class Ingredient(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name



class RecipeIngredient(models.Model):
    
    quantity = models.CharField(max_length=50)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.quantity} of {self.ingredient.name} for {self.recipe.name}"
    
    def get_absolute_url(self):
        return reverse('recipe_detail', args=[str(self.recipe.pk)])