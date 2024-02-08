from django import forms
from .models import UserProfile

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['bio', 'favorite_products', 'profile_picture']
        exclude = ['likes_received', 'likes_given']