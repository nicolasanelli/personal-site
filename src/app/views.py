from django.shortcuts import render
from .models import *

def index(request):  
  homepage = Homepage.objects.first()
  links = HomepageLink.objects.filter(show=True).order_by('order').all()
  context = {
    'homepage': homepage,
    'links': links
  }
  return render(request, "index.html", context=context)

def blog(request):
    return render(request, "blog_list.html")

def post(request, slug):
    return render(request, "blog_post.html")

def portfolio(request):
    return render(request, "portfolio.html")
