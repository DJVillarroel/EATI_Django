from typing import Any
from django.shortcuts import render, redirect
from .models import Post, Comment
from .forms import CommentForm, PostForm
from django.views.generic import TemplateView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy, reverse


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
        comments = Comment.objects.filter(post=post).order_by('-id') 
        context['comments'] = comments
        context['comment_form'] = CommentForm()  # Initialize an empty comment form
        return context
    
    def post(self, request, *args, **kwargs):
        post = self.get_object()
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            # Redirect to the same post detail page after adding the comment
            return redirect(reverse('imageboard:detail', kwargs={'pk': post.pk}))
        else:
            # If form is invalid, re-render the page with errors
            context = self.get_context_data()
            context['comment_form'] = form
            return self.render_to_response(context)
            
class AddPostView(LoginRequiredMixin, CreateView):
    template_name = 'imageboard/post.html'
    model = Post
    form_class = PostForm
    
    def form_valid(self, form):
        form.instance.author = self.request.user 
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse_lazy('imageboard:detail', kwargs={'pk': self.object.pk})
    
    