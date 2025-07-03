from .models import Comment
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)
        labels = {
            'body': ''  # Set to an empty string to remove "Body:"
        }
