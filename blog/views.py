from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Comment
from .forms import CommentForm
from django.contrib.auth.decorators import login_required
from .models import SavedPost


def blog(request):
    posts = Post.objects.filter(published=True).order_by('-created_at')
    return render(request, 'blog/blog.html', {'posts': posts})


def posts(request, slug):
    post = get_object_or_404(Post, slug=slug, published=True)
    saved = (
        SavedPost.objects.filter(user=request.user, post=post).exists()
        if request.user.is_authenticated else False
    )
    return render(
        request,
        'blog/posts.html',
        {'post': post, 'user_saved_post': saved}
    )


def like_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.user in post.likes.all():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)
    return redirect('post_detail', slug=post.slug)


@login_required
def save_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    saved_post, created = SavedPost.objects.get_or_create(
        user=request.user,
        post=post
    )
    if not created:
        saved_post.delete()  # Unsave if already saved
    return redirect('post_detail', slug=post.slug)


@login_required
def add_comment(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            return redirect('blog:posts', slug=post.slug)
    else:
        form = CommentForm()

    return render(
        request,
        'blog/posts.html',
        {'post': post, 'comment_form': form}
    )
