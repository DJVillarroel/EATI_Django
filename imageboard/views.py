from typing import Any
from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, Comment
from .forms import PostCommentForm
from django.views.generic import TemplateView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin


class HomePageView(TemplateView):
    template_name = 'imageboard/index.html'
    
    #Obtengo el contexto extrayendo todos los posts del modelo Post para mostrarlos en la plantilla.
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = Post.objects.all().order_by('-id') 
        return context
    
class PostDetailView(LoginRequiredMixin, DetailView):
    template_name = 'imageboard/detail.html'
    model = Post
    context_object_name = 'post'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = self.get_object()
        comments = Comment.objects.filter(post=post)
        context['comments'] = comments
        context['comment_form'] = PostCommentForm(post=post, author=self.request.user)
        return context
    
    def post(self, request, *args, **kwargs):
        post = self.get_object()
        form = PostCommentForm(post=post, author=request.user)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post-detail', pk=post.pk)
        else:
            context = self.get_context_data()
            context['comment_form'] = form
            return self.render_to_response(context)