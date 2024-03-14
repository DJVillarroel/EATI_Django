from django import forms
from .models import Comment, Post
from django.utils import timezone

class PostForm(forms.ModelForm):
    title = forms.CharField(label='Titulo')
    text = forms.CharField(label='Texto')
    img = forms.ImageField(label='Imagen')
    
    class Meta:
        model = Post
        fields = ['title', 'text', 'img']

class CommentForm(forms.ModelForm):
    text = forms.CharField(label='Tu comentario')
    
    class Meta:
        model = Comment
        fields = ['text']
        