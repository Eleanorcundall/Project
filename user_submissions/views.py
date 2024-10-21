from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, redirect
from .models import UserSubmission
from .forms import UserSubmissionForm

@login_required
def submit_post(request):
    print(request.method)
    if request.method == 'POST':
        user_submission_form = UserSubmissionForm(request.POST, request.FILES)
        if user_submission_form.is_valid():
            user_submission = user_submission_form.save(commit=False)
            user_submission.user = request.user 
            user_submission.save()
            return redirect('home')
    else:
        user_submission_form = UserSubmissionForm()

    return render(request, 'user_submissions/submit_post.html', {'user_submission_form': user_submission_form})

@login_required
def delete_post(request, slug):
    post = get_object_or_404(UserSubmission, slug=slug)

    if post.user != request.user:
        messages.error(request, "You are not authorized to delete this post.")
        return redirect('blog_post_detail', slug=slug)

    if request.method == "POST":
        post.delete()
        messages.success(request, "Post deleted successfully.")
        return redirect('category_view', category=post.category)
    
    return render(request, 'content_feeds/delete_post_confirm.html', {'post': post})
