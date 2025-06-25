from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from .models import BlogPost
from django.contrib.auth.decorators import login_required
from .models import SavedPost


def blog(request):
    posts = Post.objects.filter(published=True).order_by('-created_at')
    return render(request, 'blog/blog.html', {'posts': posts})


def posts(request, slug):
    post = get_object_or_404(Post, slug=slug, published=True)
    return render(request, 'blog/posts.html', {'post': post})


def like_post(request, post_id):
    post = get_object_or_404(BlogPost, id=post_id)
    if request.user in post.likes.all():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)
    return redirect('post_detail', slug=post.slug)


@login_required
def saved_posts(request):
    posts = SavedPost.objects.filter(user=request.user).select_related('post')
    return render(request, 'blog/saved_posts.html', {'saved_posts': posts})
