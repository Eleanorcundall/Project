from django.shortcuts import render, get_object_or_404
from .models import BlogPost
from user_submissions.models import UserSubmission


def home_view(request): 
    blog_posts = BlogPost.objects.filter(status='published')
    user_submissions = UserSubmission.objects.filter(status='published')
    
    all_posts = list(blog_posts) + list(user_submissions)

    
    all_posts.sort(key=lambda x: x.created_at, reverse=True)

    
    return render(request, 'home_feed/home_feed.html', {'all_posts': all_posts})


def blog_post_detail_view(request, slug):
    blog_post = BlogPost.objects.filter(slug=slug, status='published').first()

    user_submission = UserSubmission.objects.filter(slug=slug, status='published').first()

    if blog_post:
        return render(request, 'home_feed/blog_post_detail.html', {'post': blog_post})
    elif user_submission:
        return render(request, 'home_feed/blog_post_detail.html', {'post': user_submission})
    else:
        raise Http404("Post not found")


def category_view(request, category):
    blog_posts = BlogPost.objects.filter(category=category, status='published')
    return render(request, 'home_feed/category_posts.html', {'blog_posts': blog_posts, 'category': category})