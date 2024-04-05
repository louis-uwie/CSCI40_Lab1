from django import forms
from .models import Recipe
from .models import RecipeImage

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['name'] 

class RecipeImageForm(forms.ModelForm):
    class Meta:
        model = RecipeImage
        fields = ['image', 'description'] 
