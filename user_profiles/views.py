from django.shortcuts import render, redirect
from .models import UserProfile
from .forms import UserProfileForm

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

    return render(request, 'user_profiles/user_profile_edit.html', {'form': form})