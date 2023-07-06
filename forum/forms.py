from .models import Comment, ForumPost
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)


class PostForm(forms.ModelForm):
    class Meta:
        model = ForumPost
        fields = ('title', 'slug', 'bikes', 'cover_image', 'content',)
        # form.instance.author = self.request.user
        # prepopulated_fields = {'slug': ('title',)}
        # prepopulated_fields = {'author': user.username}
