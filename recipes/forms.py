from .models import Comment, Recipe
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body','name_of_recipe')


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ('author', 'name_of_recipe', 'excerpt',  'slug', 'ingredients', 'instructions', 'prep_time', 'cooking_time')