from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import UserProfile
from .forms import UserProfileForm
from content_feeds.models import Like

def submit_user_profile_form(request):
    try:
        user_profile = UserProfile.objects.get(user=request.user)
    except UserProfile.DoesNotExist:
        user_profile = None

    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=user_profile)
        if form.is_valid():
            user_profile = form.save(commit=False)
            user_profile.user = request.user 
            user_profile.save()
            return redirect('home')
    else:
        form = UserProfileForm(instance=user_profile)

    return render(request, 'user_profile/user_profile_edit.html', {'form': form})


def user_profile_view(request):
    try:
        user_profile = UserProfile.objects.get(user=request.user)
    except UserProfile.DoesNotExist:
        user_profile = None
    
    current_user = request.user

    likes_given_count = Like.objects.filter(user=request.user).count()
    likes_received_count = Like.objects.filter(object_id=current_user.id).count()

    print(user_profile)
    return render(request, 'user_profile/user_profile.html', {'user_profile': user_profile, 'likes_given_count': likes_given_count, 'likes_received_count': likes_received_count})
