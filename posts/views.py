from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Q
from .models import Post, Category, Tag
from .forms import PostForm

def test_review(request):
    return HttpResponse('hello world')

def html_view(request): 
    return render(request, "base.html")

# List view for posts with filtering, pagination, and search
@login_required(login_url='users:login')
def post_list(request):
    # Get all posts ordered by creation date (newest first)
    posts_list = Post.objects.all().order_by('-created_at')
    
    # Get query parameters
    search_query = request.GET.get('search', '')
    category_id = request.GET.get('category', '')
    tag_id = request.GET.get('tag', '')
    
    # Apply search filter if provided
    if search_query:
        posts_list = posts_list.filter(
            Q(title__icontains=search_query) | 
            Q(content__icontains=search_query)
        )
    
    # Apply category filter if provided
    if category_id:
        posts_list = posts_list.filter(category_id=category_id)
    
    # Apply tag filter if provided
    if tag_id:
        posts_list = posts_list.filter(tags__id=tag_id)
    
    # Pagination - 6 posts per page
    paginator = Paginator(posts_list, 6)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)
    
    # Get all categories and tags for filter dropdowns
    categories = Category.objects.all()
    tags = Tag.objects.all()
    
    context = {
        'page_obj': page_obj,
        'categories': categories,
        'tags': tags,
        'search_query': search_query,
        'selected_category': int(category_id) if category_id else None,
        'selected_tag': int(tag_id) if tag_id else None,
    }
    
    return render(request, 'posts/post_list.html', context)

# Detail view for a specific post
@login_required(login_url='users:login')
def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    return render(request, 'posts/post_detail.html', {'post': post})

# Create view for new posts
@login_required(login_url='users:login')
def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save()
            return redirect('posts:post_detail', post_id=post.id)
    else:
        form = PostForm()
    return render(request, 'posts/post_create.html', {'form': form})