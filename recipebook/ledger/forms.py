from django import forms
from .models import Recipe
from .models import RecipeImage

'''
Form for uploading recipes.
'''
class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['name'] 


'''
Form for uploading images.
'''
class RecipeImageForm(forms.ModelForm):
    class Meta:
        model = RecipeImage
        fields = ['image', 'description'] 