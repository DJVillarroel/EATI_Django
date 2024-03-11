from django import forms

class PostCommentForm(forms.Form):
    class Meta:
        model = Comment
        fields = ['text']
        
