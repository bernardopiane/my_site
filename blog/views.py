from datetime import date
from django.http.response import HttpResponseRedirect
from django.urls import reverse

from django.shortcuts import get_object_or_404, render

from .models import Post
from .forms import CommentForm

# Import TemplateView from django.views.generic
from django.views.generic import ListView, View

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


class PostDetailView(View):
    template_name = 'blog/post-detail.html'

    def get(self, request, *args, **kwargs):
        post = get_object_or_404(Post, slug=kwargs['slug'])
        context = {
            "post": post,
            "comment_form": CommentForm(),
            "comments": post.comments.all().order_by('-id'),
        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        post = get_object_or_404(Post, slug=kwargs['slug'])
        form = CommentForm(request.POST)
        if form.is_valid():
            # Creates a new instance of the Comment model so that we can link it to the post
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return HttpResponseRedirect(reverse('post-detail-page', kwargs={'slug': post.slug}))
        else:
            context = {
                "post": post,
                "comment_form": form,
                "comments": post.comments.all().order_by('-id'),
            }
            return render(request, self.template_name, context)
