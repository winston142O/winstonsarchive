from cProfile import Profile
from urllib import request
from django.shortcuts import render

# Create your views here.

from typing import List
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import HttpResponse  ## not using so, could delete that import ##
from django.contrib.auth.models import User
from django.urls import reverse_lazy

from .forms import CommentForm

from users.views import profile
from .models import Post, Comment
from django.views.generic import (
    ListView, 
    DetailView, 
    CreateView,
    UpdateView,
    DeleteView
)

        ## Handling home page Traffic ##
            ## Adding Template Example ##


def blog(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/blog_main.html', context)

class PostListView(ListView):
    model = Post
    template_name = 'blog/blog_main.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 10

class UserProfileView(ListView):
    model = Post
    template_name = 'blog/user_profile.html'
    context_object_name = 'posts'
    paginate_by = 1

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')


class UserPostListView(ListView):
    model = Post
    template_name = 'blog/user_posts.html'
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')

def public_profile(request):
    return render(request, 'blog/public_profile.html')

class PostDetailView(DetailView):
    model = Post

class PostCreateView(CreateView):
    model = Post
    fields = ['titulo', 'contenido']

    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class CommentCreateView(CreateView):
    model = Comment
    form_class = CommentForm
    #fields = ['body']
    template_name = "blog/comment_form.html"

        
    class Meta:
        ordering=['-time']
    
    def form_valid(self, form):
        form.instance.post = Post.objects.get(pk=int(self.kwargs['pk']))
        form.instance.name = self.request.user
        return super().form_valid(form)
    
    def get_success_url(self):   
        return reverse_lazy('blog-home') 

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['titulo', 'contenido']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        else:
            return False

class CommentUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Comment
    fields = ['body']

    def form_valid(self, form):
        form.instance.name = self.request.user
        return super().form_valid(form)
    
    def get_success_url(self):   
        return reverse_lazy('blog-home') 

    def test_func(self):
        comment = self.get_object()
        if self.request.user == comment.name:
            return True
        else:
            return False    
        
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        else:
            return False
        
class CommentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Comment
    success_url = '/'

    def test_func(self):
        comment = self.get_object()
        if self.request.user == comment.name:
            return True
        else:
            return False        

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})

