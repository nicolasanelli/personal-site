from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('blog', views.BlogView.as_view(), name="blog"),
    path('post/<slug:slug>', views.PostView.as_view(), name="post"),
    path('portfolio', views.PortfolioView.as_view(), name="portfolio"),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)