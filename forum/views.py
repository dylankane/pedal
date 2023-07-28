from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic, View
from django.http import HttpResponseRedirect
from .models import ForumPost, Comment, Messages
from .forms import CommentForm, PostForm, UpdateForm, EditCommentForm, ContactForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


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
    # the posts and selecting one by slug, Then reffering to the form
    # CommentForm from forms.py, If this form is valid it triggers succes
    # message, sets author as the current user name, and saves to the Comment
    # database
    def post(self, request, slug, *args, **kwargs):
        queryset = ForumPost.objects.all()
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.all().order_by("created_on")
        pk = post.id
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

            return HttpResponseRedirect(
                reverse('post_detail', kwargs={'slug': slug, 'pk': pk}))

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
# not, with logic to add or remove the like field, and redirecting to the
# currrent page / post view.
class PostLike(View):
    def post(self, request, slug, *args, **kwargs):
        post = get_object_or_404(ForumPost, slug=slug)
        pk = post.id

        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)

        return HttpResponseRedirect(reverse('post_detail', kwargs={
            'slug': slug, 'pk': pk}))


# Function method that collects all the posts of a specific tag / text choice
# value that matches the one selected by the user. And displys them as a list.
def categories(request, cats):
    categorey_posts = ForumPost.objects.filter(
        bikes=cats) | ForumPost.objects.filter(
            bars=cats) | ForumPost.objects.filter(
                gears=cats)
    return render(
        request,
        'categories.html',
        {'cats': cats, 'categorey_posts': categorey_posts})


# Class that checks over all the posts for ones that have been liked by the
# current user, creating a list of all the posts that user has liked
class LikedList(LoginRequiredMixin, generic.ListView):
    model = ForumPost
    template_name = 'liked_list.html'
    context_object_name = "posts"
    paginate_by = 9

    def get_queryset(self):
        queryset = ForumPost.objects.filter(likes=self.request.user)
        return queryset


# Class to create a view of the posts creted by the current user,
# Targets the ForumPost model, sets a template to render to, and
# paginates by 9.
class Profile(LoginRequiredMixin, generic.ListView):
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
class CreatePost(LoginRequiredMixin, generic.CreateView):
    model = ForumPost
    template_name = 'create_post.html'
    form_class = PostForm

    # Updating / overiding the form_valid method from generic CreateView
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
        pk = self.object.id
        success_url = reverse('post_detail', kwargs={'slug': slug, 'pk': pk})
        return success_url


# Class to allow a user the update their own posts
class UpdatePost(LoginRequiredMixin, generic.UpdateView):
    model = ForumPost
    template_name = 'update_post.html'
    form_class = UpdateForm

    # Function to control a success message to appear when the form is valid
    def form_valid(self, form):
        messages.success(
            self.request, "Your bike has been successfully updated")
        return super().form_valid(form)

    # Function to get the correct url parameter to redirect the user back to
    # the post view with the updates applied
    def get_success_url(self):
        slug = self.object.slug
        pk = self.object.id
        success_url = reverse('post_detail', kwargs={'slug': slug, 'pk': pk})

        return success_url


# Class view to handle the deletion of a post
class DeletePost(LoginRequiredMixin, generic.DeleteView):
    model = ForumPost
    template_name = 'delete_post.html'
    success_url = reverse_lazy('profile')

    # Function to update the success url of the DeleteView class
    def get_success_url(self):
        messages.success(self.request, "Your bike was successfully deleted")
        success_url = reverse('profile')
        return success_url


# Class view to allow a user to edit their comments
class EditComment(LoginRequiredMixin, generic.UpdateView):
    model = Comment
    template_name = 'edit_comment.html'
    form_class = EditCommentForm

    # Function to get the success url to redirect after editing comment
    def get_success_url(self):
        messages.success(self.request, "Your Comment was successfully updated")
        slug = self.object.post.slug
        pk = self.object.post.id
        success_url = reverse('post_detail', kwargs={'slug': slug, 'pk': pk})
        return success_url


# Class to handle the deletion of a users comment
class DeleteComment(LoginRequiredMixin, generic.DeleteView):
    model = Comment
    template_name = 'delete_comment.html'
    context_object_name = 'comment'

    # Function to get the success url after the deletion of a comment
    def get_success_url(self):
        messages.success(self.request, "Your Comment was deleted successfully")
        slug = self.object.post.slug
        pk = self.object.post.id
        success_url = reverse('post_detail', kwargs={'slug': slug, 'pk': pk})
        return success_url


# Function to delete a users account, handling the success message and the
# redirect
@login_required
def delete_user(request):
    if request.method == 'POST':
        request.user.delete()
        messages.success(
            request, 'Your account has been successfully deleted.')
        return redirect('home')
    return render(request, 'delete_user.html')


class SendMessage(LoginRequiredMixin, generic.CreateView):
    model = Messages
    template_name = 'message.html'
    form_class = ContactForm
    success_url = ('about')

    def form_valid(self, form):
        messages.success(
            self.request, "Your message has been successfully sent")
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('about')

    # return HttpResponseRedirect(reverse('about'))
