from django.shortcuts import render, get_object_or_404
from .models import BlogPost

def home_view(request):
    blog_posts = BlogPost.objects.filter(status='published')
    
    return render(request, 'home_feed/home_feed.html', {'blog_posts': blog_posts})

def blog_post_detail_view(request, slug):
    blog_post = get_object_or_404(BlogPost, slug=slug, status='published')

    return render(request, 'home_feed/blog_post_detail.html', {'blog_post': blog_post})