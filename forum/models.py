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
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="forum_posts")
    slug = models.SlugField(max_length=150, unique=True)
    created_on = models.DateTimeField(auto_now=True)
    updated_on = models.DateTimeField(auto_now=True)
    cover_image = CloudinaryField('image', default="placeholder")
    content = models.TextField()
    bikes = models.CharField(max_length=20, choices=Bikes.choices, default=Bikes.NONE)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return self.title
