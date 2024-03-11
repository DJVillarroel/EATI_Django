from django.db import models
from sorl.thumbnail import ImageField
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

class Post(models.Model):
    title = models.CharField(max_length=120)
    text = models.CharField(max_length=1024)
    date = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    img = ImageField()
    
    def __str__(self):
        return self.title[0:100]
    
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField(max_length=600)
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.text