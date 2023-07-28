from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.template.defaultfilters import slugify


# Model for the main database holding the data of all the user created posts
class ForumPost(models.Model):

    # Model class defining the options of the bike type categorey within the
    # main ForumPost model
    class Bikes(models.TextChoices):
        NONE = 'N/A', 'N/A'
        ROAD = 'Road', 'Road'
        GRAVEL = 'Gravel', 'Gravel'
        CX = 'CX', 'CX'
        TOURING = 'Touring', 'Touring'
        MTB = 'MTB', 'MTB'
        DOWNHILL = 'Downhill', 'Downhill'
        FIXIE = 'Fixie', 'Fixie'
        COMMUTE = 'Commute', 'Commute'
        BMX = 'BMX', 'BMX'
        HYBRID = 'Hybrid', 'Hybrid'
        OTHER = 'Other', 'Other'

    # Model class defining the options of the handlebar type categorey within
    # the main ForumPost model
    class Bars(models.TextChoices):
        NONE = 'N/A', 'N/A'
        FLAT = 'Flat', 'Flat'
        DROP = 'Drop', 'Drop'
        ALT = 'Alt', 'Alt'
        OTHER = 'Other', 'Other'

    # Model class defining the options of the gearing type categorey within the
    # main ForumPost model
    class Gears(models.TextChoices):
        NONE = 'N/A', 'N/A'
        FIXED = 'Fixed', 'Fixed'
        ONE = '1X', '1X'
        TWO = '2X', '2X'
        THREE = '3X', '3X'
        HUB = 'Hub', 'Hub'
        OTHER = 'Other', 'Other'

    title = models.CharField(max_length=150, unique=True)
    slug = models.SlugField(max_length=150, unique=True)
    created_on = models.DateTimeField(auto_now_add=True)
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

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)


# Model for the comment section database, holding the data from all
# comments site wide
class Comment(models.Model):
    post = models.ForeignKey(
        ForumPost, on_delete=models.CASCADE, related_name='comments')
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='user_comments')
    body = models.TextField()

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return f"Comment {self.body} by {self.author}"


class Messages(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField()
    message = models.TextField()
    date_sent = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='user_message')
