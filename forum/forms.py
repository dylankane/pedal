from .models import Comment, ForumPost, Messages
from django import forms


# Form for creating a comment
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)


# Form for user to edit their own comments
class EditCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)


# Form for a logged-in user to create their own post
class PostForm(forms.ModelForm):
    class Meta:
        model = ForumPost
        fields = (
            'title',
            'bikes',
            'gears',
            'bars',
            'cover_image',
            'second_image',
            'third_image',
            'content',
            )


# Form for a user to update their own posts.
class UpdateForm(forms.ModelForm):
    class Meta:
        model = ForumPost
        fields = (
            'title',
            'bikes',
            'gears',
            'bars',
            'cover_image',
            'second_image',
            'third_image',
            'content',
            )


class ContactForm(forms.ModelForm):
    class Meta:
        model = Messages
        fields = (
            'name',
            'email',
            'message',
            )
