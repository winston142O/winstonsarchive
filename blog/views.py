from django.shortcuts import render
from django.views.generic import ListView
from .models import Post, Comment, Tag
from django.db.models import Q

class PostListView(ListView):
    model = Post
    template_name = "blog/home.html"
    context_object_name = "posts"
    ordering = ["-date_posted"]
    paginate_by = 10
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Add additional context data
        context['all_tags'] = Tag.objects.all()
        return context

def search_posts(request):
    query = request.GET.get('q')
    tags = request.GET.get('tags', '').split()

    if query or tags:
        if query=='':
            results = Post.objects.filter(tags__name__in=tags).distinct()
            
        elif tags == []:
            results = Post.objects.filter(title__icontains=query)
            
        else:
            results = Post.objects.filter(Q(title__icontains=query) & Q(tags__name__in=tags)).distinct().order_by('-date_posted')
        context = {'results': results, 'query': query, 'selected_tags':tags, 'all_tags': Tag.objects.all()}
        
    else:
        context = {'all_tags': Tag.objects.all()}
    
    return render(request, 'blog/search.html', context)

class PostDetail(ListView):
    model = Comment
    template_name = "blog/post_detail.html"
    context_object_name = "comments"
    
    def get_queryset(self):
        return Comment.objects.filter(post=self.kwargs['pk'])
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post'] = Post.objects.get(pk=self.kwargs['pk'])
        context['tags'] = context['post'].tags.all()  
        context['logged_user'] = self.request.user    
        return context
