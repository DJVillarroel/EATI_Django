from django import forms
from .models import Comment, Post
from django.utils import timezone

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'text', 'img']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
        