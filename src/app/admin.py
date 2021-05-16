from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Homepage)
admin.site.register(HomepageLink)
admin.site.register(Post)
admin.site.register(Project)
admin.site.register(ProjectLink)