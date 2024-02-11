from django.shortcuts import render
from django.views.generic import ListView
from .models import Post, Comment, Tag
from django.db.models import Q
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, Http404
from django.views import View
from django.contrib import messages

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
        return Comment.objects.filter(post=self.kwargs['pk']).order_by('-date_added')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post'] = Post.objects.get(pk=self.kwargs['pk'])
        context['tags'] = context['post'].tags.all()  
        context['logged_user'] = self.request.user    
        return context

@method_decorator(login_required, name='dispatch')
class CommentView(View):
    """ Endpoint to create a new comment. """
    
    def post(self, request, *args, **kwargs):
        # Get the post and comment text from the request
        post_id = request.POST.get('post_id')
        comment_text = request.POST.get('text')

        if not post_id or not comment_text:
            return JsonResponse({'message': 'Did not submit the appropiate parameters.'}, status=400)

        try:
            post = Post.objects.get(pk=post_id)
            
        except Post.DoesNotExist:
            raise Http404('Post not found.')

        comment = Comment.objects.create(post=post, body=comment_text, created_by=request.user)

        messages.success(request, f'Your comment has been added!')
        
        return JsonResponse({'message': 'Comment created.', 'comment_id': comment.id})
