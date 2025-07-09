# Core Django imports
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.decorators.http import require_POST
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import UpdateView, DeleteView

# Local imports
from .forms import ArticleForm, CommentForm
from .models import Post, Comment

# Views


def post_list(request):
    post_list = Post.published.all()
    paginator = Paginator(post_list, 3)
    page = request.GET.get('page', 1)

    try:
        posts = paginator.page(page)
    except (PageNotAnInteger, EmptyPage):
        posts = paginator.page(1)

    return render(request, 'blog/post_list.html', {'posts': posts})


def post_detail(request, year, month, day, slug):
    post = get_object_or_404(
        Post,
        status=Post.Status.PUBLISHED,
        slug=slug,
        publish__year=year,
        publish__month=month,
        publish__day=day
    )
    comments = post.comments.filter(active=True)
    form = CommentForm()
    return render(request, 'blog/post_detail.html', {
        'post': post,
        'comments': comments,
        'form': form
    })


@require_POST
@login_required
def post_comment(request, post_id):
    post = get_object_or_404(Post, id=post_id, status=Post.Status.PUBLISHED)
    form = CommentForm(data=request.POST)

    if form.is_valid():
        comment = form.save(commit=False)
        comment.post = post
        comment.user = request.user
        comment.email = request.user.email
        comment.save()

    return render(request, 'blog/comment.html', {
        'post': post,
        'form': form,
        'comment': comment if form.is_valid() else None
    })


class CommentUpdateView(LoginRequiredMixin, UpdateView):
    model = Comment
    fields = ['body']
    template_name = 'blog/includes/comment_edit.html'

    def get_queryset(self):
        return Comment.objects.filter(user=self.request.user)

    def get_success_url(self):
        post = self.object.post
        return reverse('blog:post_detail', args=[
            post.publish.year, post.publish.month, post.publish.day, post.slug
        ])


class CommentDeleteView(LoginRequiredMixin, DeleteView):
    model = Comment
    template_name = 'blog/includes/comment_confirm_delete.html'

    def get_queryset(self):
        return Comment.objects.filter(user=self.request.user)

    def get_success_url(self):
        post = self.object.post
        return reverse('blog:post_detail', args=[
            post.publish.year, post.publish.month, post.publish.day, post.slug
        ])


def _get_post_url(post):
    return reverse('blog:post_detail', args=[
        post.publish.year, post.publish.month, post.publish.day, post.slug
    ])


@login_required
def add_article(request):
    if not request.user.is_superuser:
        messages.error(
            request,
            'Sorry, only the staff of this shop can do that.'
        )
        return redirect('home')

    form = ArticleForm(request.POST or None, request.FILES or None)
    if request.method == 'POST':
        if form.is_valid():
            post = form.save()
            messages.success(request, 'Successfully added Article!')
            return redirect(_get_post_url(post))
        messages.error(
            request,
            'Failed to add article. Please ensure the form is valid.'
        )

    return render(request, 'blog/add_article.html', {'form': form})


@login_required
def edit_article(request, post_id):
    if not request.user.is_superuser:
        messages.error(
            request, 'Sorry, only the staff of this shop can do that.'
        )
        return redirect('home')

    post = get_object_or_404(Post, pk=post_id)
    form = ArticleForm(
        request.POST or None,
        request.FILES or None,
        instance=post
    )

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated article!')
            return redirect(_get_post_url(post))
        messages.error(
            request,
            'Failed to update article. Please ensure the form is valid.'
        )
    else:
        messages.info(request, f'You are editing {post.title}')

    return render(
        request,
        'blog/edit_article.html',
        {
            'form': form,
            'post': post
        }
    )


@login_required
def delete_article(request, post_id):
    if not request.user.is_superuser:
        messages.error(
            request, 'Sorry, only the staff of this shop can do that.'
        )
        return redirect('home')

    post = get_object_or_404(Post, pk=post_id)
    post.delete()
    messages.success(request, 'Article deleted!')
    return redirect('post_list')
