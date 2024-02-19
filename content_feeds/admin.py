from django.contrib import admin
from .models import AdPost, Like, Comment

# Register your models here.
admin.site.register(AdPost)
admin.site.register(Like)
admin.site.register(Comment)