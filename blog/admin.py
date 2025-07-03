from django.contrib import admin
from .models import Comment, Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'publish', 'status')
    list_filter = ('status', 'publish', 'author')
    search_fields = ('title', 'body')
    prepopulated_fields = {'slug': ('title',)}
# raw_id_fields = ['author']
    date_hierarchy = 'publish'
    ordering = ('status', 'publish')
    show_facets = admin.ShowFacets.ALWAYS


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = (
        'user_display', 'email', 'body', 'created', 'post', 'active'
    )
    list_filter = ('active', 'created', 'updated')
    search_fields = ('user_display', 'email', 'body')

    def user_display(self, obj):
        return obj.name.username
    user_display.short_description = 'User'
