from django.urls import path
from .views import (
    PostListView,
    search_posts,
    PostDetail,
    CommentView,
    PostCreateView,
    DeletePostView,
    post_like
)

urlpatterns = [
    path("posts/", PostListView.as_view(), name="blog-posts"),
    path("post/create/", PostCreateView.as_view(), name="create-post"),
    path('post/<int:pk>/delete/', DeletePostView.as_view(), name='post_delete'),
    path("post/detail/<int:pk>/", PostDetail.as_view(), name="post-detail"),
    path("comment/post/", CommentView.as_view(), name="post-comment"),
    path('post/<int:pk>/like/', post_like, name='post-like'),
    path('search/', search_posts, name='search_posts'),
]