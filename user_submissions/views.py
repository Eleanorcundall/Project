from django.shortcuts import render, redirect
from .models import UserSubmission
from .forms import UserSubmissionForm

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
