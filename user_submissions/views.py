from django.shortcuts import render, redirect
from .models import UserSubmission
from .forms import UserSubmissionForm

def submit_post(request):
    if request.method == 'POST':
        form = UserSubmissionForm(request.POST, request.FILES)
        if form.is_valid():
            user_submission = form.save(commit=False)
            user_submission.user = request.user 
            user_submission.save()
            return redirect('home')
    else:
        form = UserSubmissionForm()

    return render(request, 'user_submissions/submit_post.html', {'form': form})
