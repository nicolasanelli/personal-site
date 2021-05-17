from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, "index.html")

def blog(request):
    return render(request, "blog_list.html")

def post(request, slug):
    return render(request, "blog_post.html")

def portfolio(request):
    return render(request, "portfolio.html")
