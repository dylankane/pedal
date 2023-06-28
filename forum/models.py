from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.


class ForumPost(models.Model):
    title = models.CharField(max_length=150, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="forum_posts")
    slug = models.SlugField(max_length=150, unique=True)
    created_on = models.DateTimeField(auto_now=True)
    updated_on = models.DateTimeField(auto_now=True)
    cover_image = CloudinaryField('image', default="placeholder")
    content = models.TextField()

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return self.title
