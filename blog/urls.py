from django.urls import path
from .views import (
    PostListView,
    search_posts,
    PostDetail
)

urlpatterns = [
    path("posts/", PostListView.as_view(), name="blog-posts"),
    path("post/detail/<int:pk>/", PostDetail.as_view(), name="post-detail"),
    path('search/', search_posts, name='search_posts'),
]