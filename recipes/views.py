from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Recipe
from .forms import CommentForm

# Create your views here.
class PostList(generic.ListView):
    queryset = Recipe.objects.all()
    template_name = "recipes/index.html"
    paginate_by = 6

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
        comment_form = CommentForm()

        return render(request, 
        "recipes/post_detail.html", 
        {
        "recipe": post,
        "comments": comments,
        "comment_count": comment_count,
        "comment_form": comment_form, 
        },
        )