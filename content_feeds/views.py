from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib.contenttypes.models import ContentType
from django.http import JsonResponse
from .models import BlogPost, Like
from .forms import LikePostForm
from user_submissions.models import UserSubmission


def home_view(request): 
    blog_posts = BlogPost.objects.filter(status='published')
    user_submissions = UserSubmission.objects.filter(status='published')
    
    all_posts = list(blog_posts) + list(user_submissions)

    
    all_posts.sort(key=lambda x: x.created_at, reverse=True)

    
    return render(request, 'content_feeds/home_feed.html', {'all_posts': all_posts})


def blog_post_detail_view(request, slug):
    blog_post = BlogPost.objects.filter(slug=slug, status='published').first()

    user_submission = UserSubmission.objects.filter(slug=slug, status='published').first()

    if blog_post:
        return render(request, 'content_feeds/blog_post_detail.html', {'post': blog_post})
    elif user_submission:
        return render(request, 'content_feeds/blog_post_detail.html', {'post': user_submission})
    else:
        raise Http404("Post not found")


def category_view(request, category):
    blog_posts = BlogPost.objects.filter(category=category, status='published')

    user_submissions = UserSubmission.objects.filter(category=category, status='published')

    all_posts = list(blog_posts) + list(user_submissions)

    all_posts.sort(key=lambda x: x.created_at, reverse=True)
    return render(request, 'content_feeds/category_posts.html', {'all_posts': all_posts, 'category': category})


@login_required
def like_post(request, post_id):
    post = get_object_or_404(UserSubmission, id=post_id)
    user = request.user

    if request.method == 'POST':
        form = LikePostForm(request.POST)
        if form.is_valid():

            if Like.objects.filter(user=user, content_type__model='usersubmission', object_id=post_id).exists():
                return JsonResponse({'error': 'You have already liked this post'}, status=400)
            else:
                like = form.save(commit=False)
                like.user = user
                like.content_type = ContentType.objects.get_for_model(post)
                like.object_id = post.id
                like.save()
                print("Post liked!")
                return redirect('blog_post_detail', slug=post.slug)

    else:
        form = LikePostForm()

    return render(request, 'blog_post_detail.html', {'form': form})