from django.shortcuts import render, get_object_or_404
from .models import Post


def blog(request):
    posts = Post.objects.filter(published=True).order_by('-created_at')
    return render(request, 'blog/blog.html', {'posts': posts})


def posts(request, slug):
    post = get_object_or_404(Post, slug=slug, published=True)
    return render(request, 'blog/posts.html', {'post': post})
