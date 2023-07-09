from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.template.defaultfilters import slugify

# Create your models here.


class ForumPost(models.Model):

    class Bikes(models.TextChoices):
        NONE = 'Unknown', 'Unknown'
        ROAD = 'Road', 'Road'
        MTB = 'Mtb', 'Mtb'
        GRAVEL = 'Gravel', 'Gravel'
        FIXIE = 'Fixie', 'Fixie'
        TOURING = 'Touring', 'Touring'
        BMX = 'BMX', 'BMX'
        HYBRID = 'Hybrid', 'Hybrid'
        OTHER = 'Other', 'Other'

    class Bars(models.TextChoices):
        NONE = 'Unknown', 'Unknwon'
        FLAT = 'Flat', 'Flat'
        DROP = 'Drop', 'Drop'
        ALT = 'Alt', 'Alt'
        OTHER = 'Other', 'Other'

    class Gears(models.TextChoices):
        NONE = 'Unknown', 'Unknwon'
        FIXED = 'FIXED', 'FIXED'
        ONE = '1X', '1X'
        TWO = '2X', '2X'
        THREE = '3X', '3X'
        OTHER = 'Other', 'Other'

    title = models.CharField(max_length=150, unique=True)
    slug = models.SlugField(max_length=150, unique=True)
    created_on = models.DateTimeField(auto_now=True)
    updated_on = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="forum_posts")
    bikes = models.CharField(
        max_length=20, choices=Bikes.choices, default=Bikes.NONE)
    bars = models.CharField(
        max_length=20, choices=Bars.choices, default=Bikes.NONE)
    gears = models.CharField(
        max_length=20, choices=Gears.choices, default=Bikes.NONE)
    cover_image = CloudinaryField('image', default="placeholder")
    second_image = CloudinaryField('image', default="placeholder")
    third_image = CloudinaryField('image', default="placeholder")
    content = models.TextField()
    likes = models.ManyToManyField(
        User, related_name='forum_like', blank=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title

    def number_of_likes(self):
        return self.likes.count()

    def save(self, *args, **kwargs):  # new
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)


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
