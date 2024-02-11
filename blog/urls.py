from django.urls import path
from .views import (
    PostListView,
    search_posts,
    PostDetail,
    CommentView
)

urlpatterns = [
    path("posts/", PostListView.as_view(), name="blog-posts"),
    path("post/detail/<int:pk>/", PostDetail.as_view(), name="post-detail"),
    path("comment/post/", CommentView.as_view(), name="post-comment"),
    path('search/', search_posts, name='search_posts'),
]