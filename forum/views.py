from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import ForumPost


class PostList(generic.ListView):
    model = ForumPost
    queryset = ForumPost.objects.order_by('-created_on')
    template_name = 'index.html'
    context_object_name = "posts"
    paginate_by = 9


class PostDetail(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = ForumPost.objects.all()
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.all().order_by("created_on")
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request, 
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "liked": liked
            },
        )
