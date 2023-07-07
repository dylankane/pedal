from .models import Comment, ForumPost
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)


class PostForm(forms.ModelForm):
    class Meta:
        model = ForumPost
        fields = (
            'title', 'slug', 'bikes', 'gears', 'bars', 'cover_image', 'content',)


class UpdateForm(forms.ModelForm):
    class Meta:
        model = ForumPost
        fields = (
            'title', 'slug', 'bikes', 'gears', 'bars', 'cover_image', 'content',)
