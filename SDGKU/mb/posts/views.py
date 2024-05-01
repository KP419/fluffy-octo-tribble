from django.views.generic import (
    ListView,
    CreateView,
    DeleteView
)

# Create your views here.
from .models import Post

class PostListView(ListView):
    template_name = "posts/list.html"
    model = Post
    

class PostDetailView(DeleteView):
    template_name = "posts/detail.html"
    model = Post

class PostCreateView(CreateView):
    template_name = "posts/new.html"
    model = Post
    fields = ["title", "subtitle", "body"]