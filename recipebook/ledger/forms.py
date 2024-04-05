from django import forms
from .models import Recipe, RecipeImage

class RecipeForm(forms.Form):
    name = forms.CharField(label = 'Author Name', max_length=100)
    

class RecipeImageForm(forms.Form):
    name = forms.Char