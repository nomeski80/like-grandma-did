from django.contrib import admin
from .models import Recipe, Comment
from django_summernote.admin import SummernoteModelAdmin

@admin.register(Recipe)
class RecipesAdmin(SummernoteModelAdmin):

    list_display = ('name_of_recipe', 'slug', 'status')
    search_fields = ['name_of_recipe']
    list_filter = ('status',)
    prepopulated_fields = {'slug': ('name_of_recipe',)}
    summernote_fields = ('ingredients', 'instructions')

# Register your models here.


# Register your models here.

admin.site.register(Comment)
