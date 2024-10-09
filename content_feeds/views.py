from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib.contenttypes.models import ContentType
from django.http import JsonResponse
from .models import AdPost, Like, Comment
from .forms import LikePostForm, CommentForm
from user_submissions.models import UserSubmission


def home_view(request): 
    ad_posts = AdPost.objects.filter(status='published')
    print("Hello!")
    print(ad_posts)
    user_submissions = UserSubmission.objects.filter(status='published')
    
    all_posts = list(ad_posts) + list(user_submissions)

    
    all_posts.sort(key=lambda x: x.created_at, reverse=True)

    
    return render(request, 'content_feeds/home_feed.html', {'all_posts': all_posts})


def blog_post_detail_view(request, slug):
    ad_post = AdPost.objects.filter(slug=slug, status='published').first()

    user_submission = UserSubmission.objects.filter(slug=slug, status='published').first()

    if ad_post:
        post = ad_post
        post_type = 'ad_post'
    elif user_submission:
        post = user_submission
        post_type = 'user_submission'
        author = user_submission.user
        author_id = author.id
        author_username = author.username
        comment = Comment.objects.filter(post=user_submission)
    else:
        raise Http404("Post not found")
    
    comments = Comment.objects.filter(post=post)

    return render(request, 'content_feeds/blog_post_detail.html', {'post': post, 'post_type': post_type,'author_id': author_id, 'author_username': author_username, 'comments': comments})



def category_view(request, category):
    ad_posts = AdPost.objects.filter(category=category, status='published')

    user_submissions = UserSubmission.objects.filter(category=category, status='published')

    all_posts = list(ad_posts) + list(user_submissions)

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
                like.object_owner_id = post.user_id
                like.save()
                print("Post liked!")
                return redirect('blog_post_detail', slug=post.slug)

    else:
        form = LikePostForm()

    return render(request, 'blog_post_detail.html', {'form': form})


@login_required
def comment_on_post(request, post_id):
    post = get_object_or_404(UserSubmission, id=post_id)
    
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.user = request.user
            comment.post = post
            comment.save()
            return redirect('blog_post_detail', slug=post.slug)
   
    return render(request, 'blog_post_detail.html', {'post': post})

def edit_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id, user=request.user)

    if request.method == 'POST':
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            return redirect('blog_post_detail', slug=comment.post.slug)
    else:
        form = CommentForm(instance=comment)

    return render(request, 'content_feeds/edit_comment.html', {'form': form, 'comment': comment})
