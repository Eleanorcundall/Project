from django import forms
from .models import Like

class LikePostForm(forms.Modelform):
    class Meta:
        model = Like
        fields = []
