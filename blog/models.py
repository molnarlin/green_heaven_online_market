from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.conf import settings


class Post(models.Model):
    class Status(models.TextChoices):
        DRAFT = 'draft', 'Draft'
        PUBLISHED = 'published', 'Published'
        ARCHIVED = 'archived', 'Archived'
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    content = models.TextField()
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='posts'
    )
    image = models.ImageField(upload_to='blog_images/', blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now)
    published = models.BooleanField(default=False)
    likes = models.ManyToManyField(
        User,
        related_name='liked_posts',
        blank=True
    )
    status = models.CharField(
        max_length=10,
        choices=Status.choices,
        default=Status.DRAFT
    )

    class Meta:
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['-created_at']),
        ]

    def __str__(self):
        return self.title

    def total_likes(self):
        return self.likes.count()


class Comment(models.Model):
    post = models.ForeignKey(
        'Post',
        on_delete=models.CASCADE,
        related_name='comments'
    )
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.author} on {self.post}"


class SavedPost(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey('Post', on_delete=models.CASCADE)
    saved_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} saved {self.post}"
