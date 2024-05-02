from django.shortcuts import TemplateView

    
class PostListView(TemplateView):
    template_name = "pages/list.html"

class PostDetailView(TemplateView):
    template_name = "pages/detail.html"
    
class PostCreateView(TemplateView):
    template_name = "pages/new.html"

# Create your views here.
