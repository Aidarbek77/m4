from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Post

def test_review(request):
    return HttpResponse('hello world')

def html_view(request): 
    return render(request, "base.html")

# List view for posts
def post_list(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'posts/post_list.html', {'posts': posts})

# Detail view for a specific post
def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    return render(request, 'posts/post_detail.html', {'post': post})