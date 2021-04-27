from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('blog', views.blog, name="blog"),
    path('portfolio', views.portfolio, name="portfolio"),
]
