from django import forms
from .models import Comment

class PostCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
        
    def __init__(self, post, author, *args, **kwargs):
        self.post = post
        self.author = author
        super(PostCommentForm, self).__init__(*args, **kwargs)

    def save(self, commit=True):
        comment = super(PostCommentForm, self).save(commit=False)
        comment.post = self.post
        comment.author = self.author
        if commit:
            comment.save()
        return comment