from django.shortcuts import render
from django.views import generic
from .models import ForumPost


class PostList(generic.ListView):
    model = ForumPost
    queryset = ForumPost.objects.order_by('-created_on')
    template_name = 'index.html'
    context_object_name = "posts"
    paginate_by = 9
