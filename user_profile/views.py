from django.shortcuts import render, redirect, get_object_or_404
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

    print(current_user)

    likes_given_count = Like.objects.filter(user=current_user).count()
    likes_received_count = Like.objects.filter(object_owner=current_user).count()

    print(user_profile)
    return render(request, 'user_profile/user_profile.html', {'user_profile': user_profile, 'likes_given_count': likes_given_count, 'likes_received_count': likes_received_count})


def other_user_profile_view(request, user_id):
    user = get_object_or_404(User, id=user_id)
    user_profile = get_object_or_404(UserProfile, user=user)


    likes_given_count = Like.objects.filter(user=user).count()
    likes_received_count = Like.objects.filter(object_owner=user).count()

    return render(request, 'user_profile/other_user_profile.html', {
    'user_profile': user_profile,
    'likes_given_count': likes_given_count,
    'likes_received_count': likes_received_count
    })
