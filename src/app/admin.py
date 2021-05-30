from django.contrib import admin
from .models import *
from django_summernote.admin import SummernoteModelAdmin

class PostAdmin(SummernoteModelAdmin):
  summernote_fields = 'markdown_text'

# Register your models here.
admin.site.register(Homepage)
admin.site.register(HomepageLink)
admin.site.register(Post, PostAdmin)
admin.site.register(Project)
admin.site.register(ProjectLink)