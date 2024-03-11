from typing import Any
from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, Comment
from .forms import PostCommentForm
from django.views.generic import TemplateView, DetailView

class HomePageView(TemplateView):
    template_name = 'imageboard/index.html'
    
    #Obtengo el contexto extrayendo todos los posts del modelo Post para mostrarlos en la plantilla.
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = Post.objects.all().order_by('-id') 
        return context
    
class PostDetailView(DetailView):
    template_name = 'imageboard/detail.html'
    model = Post
    context_object_name = 'post'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = self.get_object()
        comments = Comment.objects.filter(post=post)
        context['comments'] = comments
        return context
    
def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    comments = Comment.objects.filter(post=post)
    form = PostCommentForm(request.POST or None)  # Corrected here
    if request.method == 'POST':
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user  
            comment.save()
            return redirect('post_detail', post_id=post_id)  # Corrected here
    return render(request, 'imageboard/detail.html', {'post': post, 'comments': comments, 'form': form})