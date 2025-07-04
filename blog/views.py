from django.shortcuts import render, get_object_or_404
from .models import Post, Comment
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView
from django.views.decorators.http import require_POST
from .forms import CommentForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy, reverse


class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'
    paginate_by = 3

    def get_queryset(self):
        return Post.objects.filter(status='published').order_by('publish')


def post_list(request):
    post_list = Post.published.all()
    paginator = Paginator(post_list, 3)
    page_number = request.GET.get('page', 1)
    try:
        posts = paginator.page(page_number)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
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
    return render(
        request,
        'blog/post_detail.html',
        {
            'post': post,
            'comments': comments,
            'form': form
        }
    )


@require_POST
def post_comment(request, post_id):
    post = get_object_or_404(Post, id=post_id, status=Post.Status.PUBLISHED)
    comment = None
    form = CommentForm(data=request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.post = post
        comment.user = request.user  # Ensures it's the logged-in user
        comment.email = request.user.email
        comment.save()
        return render(
            request,
            'blog/comment.html',
            {
                'post': post,
                'form': form,
                'comment': comment
            }
        )


class CommentUpdateView(LoginRequiredMixin, UpdateView):
    model = Comment
    fields = ['body']
    template_name = 'blog/includes/comment_edit.html'

    def get_queryset(self):
        return Comment.objects.filter(user=self.request.user)

    def form_valid(self, form):
        response = super().form_valid(form)
        # Optionally flash a success message here
        return response

    def get_success_url(self):
        post = self.object.post
        return reverse('blog:post_detail', args=[
            post.publish.year,
            post.publish.month,
            post.publish.day,
            post.slug
        ])


class CommentDeleteView(LoginRequiredMixin, DeleteView):
    model = Comment
    template_name = 'blog/includes/comment_confirm_delete.html'
    success_url = reverse_lazy('blog:post_detail')

    def get_queryset(self):
        return Comment.objects.filter(user=self.request.user)

    def get_success_url(self):
        post = self.object.post
        return reverse('blog:post_detail', args=[
            post.publish.year,
            post.publish.month,
            post.publish.day,
            post.slug
        ])
