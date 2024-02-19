from django import forms
from .models import Like, Comment

class LikePostForm(forms.ModelForm):
    class Meta:
        model = Like
        fields = []

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']