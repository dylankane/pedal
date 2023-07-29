from django.contrib import admin
from .models import ForumPost, Comment, Messages


@admin.register(ForumPost)
class ForumPostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'author', 'created_on', 'updated_on')
    list_filter = ('created_on', 'updated_on')
    search_fields = ('title', 'author__username')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'author', 'body', 'created_on')
    list_filter = ('created_on', 'updated_on')
    search_fields = ('post__title', 'author__username')


@admin.register(Messages)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('author', 'name', 'email', 'message', 'date_sent')
    list_filter = ('author', 'email', 'date_sent')
    search_fields = ('author__username', 'name','date_sent')
