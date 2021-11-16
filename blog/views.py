from datetime import date

from django.shortcuts import render

# Create your views here.

# Dictionary with dummy data for posts including slug, title, created_date and author
all_posts = [
    {
        "title": "My first post",
        "slug": "my-first-post",
        "date": date(2020, 1, 1),
        "author": "John Doe",
        "image": "1.png",
        "excert": "My first blog post",
        "content": """Lorem ipsum dolor sit amet, consectetur adipisicing elit. Dolor
          explicabo sequi est officia modi, magni beatae quo iusto totam cum
          alias laboriosam, maxime suscipit excepturi impedit qui dolorum esse
          ipsum"""
    },
    {
        "title": "My second post",
        "slug": "my-second-post",
        "date": date(2020, 1, 1),
        "author": "Jane Doe",
        "image": "2.jpg",
        "excert": "My second blog post",
        "content": """Lorem ipsum dolor sit amet, consectetur adipisicing elit. Dolor
          explicabo sequi est officia modi, magni beatae quo iusto totam cum
          alias laboriosam, maxime suscipit excepturi impedit qui dolorum esse
          ipsum"""
    },
    {
        "title": "My third post",
        "slug": "my-third-post",
        "date": date(2020, 1, 1),
        "author": "Jack Doe",
        "image": "3.png",
        "excert": "My third blog post",
        "content": """Lorem ipsum dolor sit amet, consectetur adipisicing elit. Dolor
          explicabo sequi est officia modi, magni beatae quo iusto totam cum
          alias laboriosam, maxime suscipit excepturi impedit qui dolorum esse
          ipsum"""
    },
]


def starting_page(request):
    sorted_posts = sorted(all_posts, key=lambda k: k['date'], reverse=True)
    latest_posts = sorted_posts[-3:]
    return render(request, 'blog/index.html', {'posts': latest_posts})


def posts(request):
    return render(request, 'blog/all-posts.html')


def post_detail(request, slug):
    return render(request, 'blog/post-detail.html')
