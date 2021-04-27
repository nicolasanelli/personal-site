from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("Home page!")

def blog(request):
    return HttpResponse("Blog page!")

def portfolio(request):
    return HttpResponse("Portfolio page!")
