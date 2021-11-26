from datetime import date

from django.shortcuts import get_object_or_404, render

from .models import Post

# Create your views here.

# Dictionary with dummy data for posts including slug, title, created_date and author
all_posts = []


def starting_page(request):
    # Fetch the 3 latest posts
    latest_posts = Post.objects.all().order_by('-date')[:3]
    return render(request, 'blog/index.html', {'posts': latest_posts})


def posts(request):
    all_posts = Post.objects.all().order_by('-date')
    return render(request, 'blog/all-posts.html', {'posts': all_posts})


def post_detail(request, slug):
    post_by_slug = get_object_or_404(Post, slug=slug)
    return render(request, 'blog/post-detail.html', {'post': post_by_slug})
