from django import forms
from .models import Like

class LikePostForm(forms.ModelForm):
    class Meta:
        model = Like
        fields = []
