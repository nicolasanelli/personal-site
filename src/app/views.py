from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("Home page!")

def blog(request):
    return HttpResponse("Blog page!")

def post(request, slug):
    return HttpResponse(f"Post \"{slug}\" page!")

def portfolio(request):
    return HttpResponse("Portfolio page!")
