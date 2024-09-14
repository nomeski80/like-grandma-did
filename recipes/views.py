from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.contrib import messages
from .models import Recipe
from .forms import CommentForm, RecipeForm


# Create your views here.
class PostList(generic.ListView):
    queryset = Recipe.objects.all()
    template_name = "recipes/index.html"
    paginate_by = 6

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["recipe_form"] = RecipeForm()
        return context

    def post(self, request, *args, **kwargs):
        recipe_form = RecipeForm(request.POST)
        if recipe_form.is_valid():
            recipe_form.save()
            return redirect("add your redirect after form submission")
        else:
            context = self.get_context_data()
            context["recipe_form"] = recipe_form
            return render(request, self.template_name, context)    
    



def post_detail(request, slug):
    """
    Display an individual :model:`recipe.Post`.

    **Context**

    ``post``
        An instance of :model:`recipe.Post`.

    **Template:**

    :template:`recipe/post_detail.html`
    """
    queryset = Recipe.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    comments = post.comments.all().order_by("-created_on")
    
    comment_count = post.comments.filter(approved=True).count()
    if request.method == "POST":
        
    
        comment_form = CommentForm(data=request.POST)
       
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.body = comment_form.data["body"]
            comment.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Comment submitted and awaiting approval'
    )
            
    comment_form = CommentForm()
    
    
    return render(
        request,
        "recipes/post_detail.html",
        {
            "recipe": post,
            "comments": comments,
            "comment_count": comment_count,
            "comment_form": comment_form,
        }
    )
    

    recipe_form = RecipeForm ()

    return render (
        request, 
        "recipes/models.py",
        {
            "recipe": form,
            "name_of_recipe": name_of_recipe,
            "ingredients": ingredients,
            "instructions": instructions,
            "prep_time": prep_time,
        }
    )