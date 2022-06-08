from django.urls import path, include
from django.urls import path
from .views import (
    CommentDeleteView,
    CommentUpdateView,
    PostListView, 
    PostDetailView, 
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    UserPostListView,
    UserProfileView,
    public_profile,
    CommentCreateView
)

from . import views

urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    path('user-posts/<str:username>', UserPostListView.as_view(), name='user-posts'),
    path('user/<str:username>', UserProfileView.as_view(), name='user-profile'),
    path('markdownx/', include('markdownx.urls')),    
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/comment/new/', CommentCreateView.as_view(), name='comment-create'),  
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('comment/<int:pk>/update/', CommentUpdateView.as_view(), name='comment-update'),
    path('comment/<int:pk>/delete/', CommentDeleteView.as_view(), name='comment-delete'),
    path('about/', views.about, name='blog-about'), # pretty sure this link doesn't do anything #
]