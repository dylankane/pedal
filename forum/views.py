from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.http import HttpResponseRedirect
from .models import ForumPost
from .forms import CommentForm, PostForm
from django.contrib import messages
from django.contrib.auth.models import User


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
                "liked": liked,
                "comment_form": CommentForm()
            },
        )

    def post(self, request, slug, *args, **kwargs):
        queryset = ForumPost.objects.all()
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.all().order_by("created_on")
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        comment_form = CommentForm(data=request.POST)

        if comment_form.is_valid():
            messages.success(
                request, "Your comment has been successfully posted")
            comment_form.instance.author = request.user
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()

        else:
            comment_form = CommentForm

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "liked": liked,
                "comment_form": CommentForm()
            },
        )


class PostLike(View):
    def post(self, request, slug):
        post = get_object_or_404(ForumPost, slug=slug)

        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)

        return HttpResponseRedirect(reverse('post_detail', args=[slug]))


class CreatePost(generic.CreateView):
    model = ForumPost
    template_name = 'create_post.html'
    form_class = PostForm

    def form_valid(self, form):
        messages.success(
            self.request, "Your bike has been successfully posted")
        form.instance.author = self.request.user
        return super().form_valid(form)

    # def create(self, request):
    #     author.instance = self.request.user