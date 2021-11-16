

from django.urls.conf import path

from . import views


urlpatterns = [
    path("", views.starting_page, name="starting-page"),
    path("posts", views.posts, name="posts-page"),
    # Path to the post slug (e.g. /posts/my-first-post)
    path("posts/<slug:slug>", views.post_detail, name="post-detail-page"),
]
