from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.


class ForumPost(models.Model):

    class Bikes(models.TextChoices):
        NONE = 'N/A', 'N/A'
        ROAD = 'RD', 'Road'
        MTB = 'MTB', 'Mtb'
        GRAVEL = 'GRVL', 'Gravel'
        FIXIE = 'FIX', 'Fixie'
        TOURING = 'TR', 'Touring'
        BMX = 'BMX', 'Bmx'
        HYBRID = 'HYB', 'Hybrid'

    title = models.CharField(max_length=150, unique=True)
    slug = models.SlugField(max_length=150, unique=True)
    created_on = models.DateTimeField(auto_now=True)
    updated_on = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="forum_posts")
    bikes = models.CharField(
        max_length=20, choices=Bikes.choices, default=Bikes.NONE)
    cover_image = CloudinaryField('image', default="placeholder")
    content = models.TextField()
    
    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(
        ForumPost, on_delete=models.CASCADE, related_name='comments')
    created_on = models.DateTimeField(auto_now=True)
    updated_on = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='user_comments')
    body = models.TextField()

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return f"Comment {self.body} by {self.author}"
