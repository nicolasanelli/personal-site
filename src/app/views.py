from django.shortcuts import render
from django.views import generic
from .models import *

def index(request):
  homepage = Homepage.objects.first()
  links = HomepageLink.objects.filter(show=True).order_by('order').all()
  context = {
    'homepage': homepage,
    'links': links
  }
  return render(request, "index.html", context=context)

class BlogView(generic.ListView):
  model = Post
  template_name = "blog_list.html"
  paginate_by = 5

  extra_context={
    'homepage': Homepage.objects.first(),
    'recent_posts': Post.objects.all()[:10]
  }

  def get_queryset(self):
    return self.model.objects.filter(show=True)

class PostView(generic.DetailView):
  model = Post
  template_name = "blog_post.html"

  extra_context={
    'homepage': Homepage.objects.first(),
    'recent_posts': Post.objects.all()[:10]
  }

def portfolio(request):
    return render(request, "portfolio.html")
