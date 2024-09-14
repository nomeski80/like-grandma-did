from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

STATUS = ((0, "Draft"), (1, "Published"))

# Create your models here.
class Recipe(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="recipe_posts")
    name_of_recipe = models.CharField(max_length=200, unique=True)
    created_on = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=200, unique=True)
    featured_image = CloudinaryField('image', default='placeholder')
    ingredients = models.TextField(unique=True)
    instructions = models.TextField(unique=True)
    status = models.IntegerField( choices=STATUS, default=0)
    excerpt = models.TextField(max_length=200, blank=True)
    prep_time = models.IntegerField(default=1, choices=((i,i) for i in range(1, 101)))
    cooking_time = models.IntegerField(default=1, choices=((i,i) for i in range(1, 101)))
    
    class Meta:
        ordering = ["-created_on"]
        
    def __str__(self):
        return f"{self.name_of_recipe} | written by {self.author}"
            


class Comment(models.Model):
    name_of_recipe = models.ForeignKey(
        Recipe, on_delete=models.CASCADE, related_name="comments")
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="commenter")
    body = models.TextField()
    approved = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ["-created_on"]
        
    def __str__(self):
        return f"Comment {self.body} by {self.author}"
