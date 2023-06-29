from django.shortcuts import render
from django.views import generic
from .models import ForumPost


# Create your views here.
class PostList(generic.ListView):
    model = ForumPost
    queryset = ForumPost.objects.order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 9
