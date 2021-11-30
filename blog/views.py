from datetime import date

from django.shortcuts import get_object_or_404, render

from .models import Post
from .forms import CommentForm

# Import TemplateView from django.views.generic
from django.views.generic import TemplateView, ListView, DetailView

# Create your views here.


class StartingPageView(ListView):
    model = Post
    template_name = 'blog/index.html'
    context_object_name = 'posts'
    ordering = ['-date']
    # Fetch the 3 latests posts

    def get_queryset(self):
        queryset = super().get_queryset()
        data = queryset[:3]
        return data


class AllPostsView(ListView):
    model = Post
    template_name = 'blog/all-posts.html'
    context_object_name = 'posts'
    ordering = ['-date']


class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post-detail.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comment_form'] = CommentForm()
        return context
