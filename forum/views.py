from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic, View
from django.http import HttpResponseRedirect
from .models import ForumPost, Comment
from .forms import CommentForm, PostForm, UpdateForm, EditCommentForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.urls import reverse_lazy


# Class to show all posts on the homepage as list, targets the ForumPost model,
# gets all posts and orders them by creation date,
# paginates page by 9 posts, and renders to template.
class PostList(generic.ListView):
    model = ForumPost
    queryset = ForumPost.objects.order_by('-created_on')
    template_name = 'index.html'
    context_object_name = "posts"
    paginate_by = 9


# Class that handles the view of each individual post,
# with like and commenting functionality
class PostDetail(View):

    # Updating the get method for generic View, creates object of all posts,
    # selects the one being viewed by the slug field, also gets all comments
    # on this post, and checks if user has liked this post. Then renders all
    # info to the template.
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

    # Updates the post method on the generic view, again collecting a set of
    # the posts and selecting by one by slug, Then refering to the form
    # CommentForm from forms.py, If this form is valid it triggers succes
    # message, sets author as the current user name, and saves to the Comment
    # database
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
            'post_detail.html',
            {
                "post": post,
                "comments": comments,
                "liked": liked,
                "comment_form": CommentForm()
            },
        )


# Class to handle the like functionality of the posts,
# retrievs the object/post by its slug field, and checks if user has liked or
#  not, with logic to add or remove the like field, and redirecting to the
#   currrent page / post view.
class PostLike(View):
    def post(self, request, slug):
        post = get_object_or_404(ForumPost, slug=slug)

        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)

        return HttpResponseRedirect(reverse('post_detail', args=[slug]))


def categories(request, cats):
    categorey_posts = ForumPost.objects.filter(bikes=cats) | ForumPost.objects.filter(bars=cats) | ForumPost.objects.filter(gears=cats)
    return render(
        request,
        'categories.html',
        {'cats': cats, 'categorey_posts': categorey_posts})


# def categories(request, cats):
#     categorey_posts = ForumPost.objects.filter(bars=cats)
#     return render(
#         request,
#         'categories.html',
#         {'cats': cats, 'categorey_posts': categorey_posts})


# def categories(request, cats):
#     categorey_posts = ForumPost.objects.filter(gears=cats)
#     return render(
#         request,
#         'categories.html',
#         {'cats': cats, 'categorey_posts': categorey_posts})


# class Categories(generic.ListView):
#     model = ForumPost
#     template_name = 'categories.html'
#     context_object_name = 'posts'
#     paginate_by = 9

#     def get_queryset(self):
#         bikes = self.request.GET.get('bikes')
#         queryset = ForumPost.objects.filter(bikes=bikes)
#         return queryset


# Class to create a view of the posts creted by the current user,
# Targets the ForumPost model, sets a template to render to, and
# paginates by 9.
class Profile(generic.ListView):
    model = ForumPost
    template_name = 'profile.html'
    context_object_name = "posts"
    paginate_by = 9

    # Sets user to the current logged in user, and retrieves a set of all posts
    # with the author field matching that name
    def get_queryset(self):
        user = self.request.user
        queryset = ForumPost.objects.filter(author=user)
        return queryset


# Class to handle user creating a post, declares the model its working on,
# the template to render to and the form from forms.py
class CreatePost(generic.CreateView):
    model = ForumPost
    template_name = 'create_post.html'
    form_class = PostForm

    # Updating / overiding the formvalid method from generic CreateView
    # When form is valid, trigger a success message and sets the author name to
    # that of the current user.
    def form_valid(self, form):
        messages.success(
            self.request, "Your bike has been successfully posted")
        form.instance.author = self.request.user
        return super().form_valid(form)

    # Updates the succuss url method of the generic CreateView.
    # Retrieving the slug of the newly created post and using it to set the
    # url, to redirect user to the post detail view of that newly created post
    def get_success_url(self):
        slug = self.object.slug
        success_url = reverse('post_detail', kwargs={'slug': slug})
        return success_url


class UpdatePost(generic.UpdateView):
    model = ForumPost
    template_name = 'update_post.html'
    form_class = UpdateForm

    def get_success_url(self):
        slug = self.object.slug
        success_url = reverse('post_detail', kwargs={'slug': slug})
        return success_url


class DeletePost(generic.DeleteView):
    model = ForumPost
    template_name = 'delete_post.html'
    success_url = reverse_lazy('profile')


class EditComment(generic.UpdateView):
    model = Comment
    template_name = 'edit_comment.html'
    form_class = EditCommentForm
    success_url = reverse_lazy('home')

    # def get_success_url(self):
    #     slug = self.object.slug
    #     success_url = reverse('post_detail', kwargs={'slug': slug})
    #     return success_url


class DeleteComment(generic.DeleteView):
    model = Comment
    template_name = 'delete_comment.html'
    context_object_name = 'comment'
    success_url = reverse_lazy('home')

    # def get_success_url(self, *args):
    #     slug = self.kwargs['post_slug']
    #     return reverse_lazy('post_detail', kwargs={'slug': slug})

    #  self.success_url = f'/{self.get_object().post.slug}'
    #  self.slug = self.get_object().post.slug
    #  return reverse_lazy('post_detail', args=[self.slug])
