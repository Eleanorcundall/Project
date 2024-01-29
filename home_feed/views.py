from django.shortcuts import render
from .models import BlogPost

def home_view(request):
    blog_posts = BlogPost.objects.all()

    return render(request, 'home_feed/home_feed.html', {'blog_posts': blog_posts})

