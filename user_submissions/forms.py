from django import forms
from .models import UserSubmission

class UserSubmissionForm(forms.ModelForm):
    class Meta:
        model = UserSubmission
        fields = ['title', 'content', 'category', 'featured_image']
        exclude = ['user', 'slug']
