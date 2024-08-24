from django.db import models
from django.contrib.auth.models import User

STATUS = ((0, "Draft"), (1, "Published"))

# Create your models here.
class Recipe(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="recipe_posts")
    name_of_recipe = models.CharField(max_length=200, unique=True)
    created_on = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=200, unique=True)
    ingredients = models.TextField()
    instructions = models.TextField()
    status = models.IntegerField(choices=STATUS, default=0)
    
