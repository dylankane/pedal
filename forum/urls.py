from . import views
from django.urls import path

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('categories/<str:cats>/', views.Categories, name='categories'),
    path('create_post/', views.CreatePost.as_view(), name='create_post'),
    path('profile/', views.Profile.as_view(), name='profile'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
    path(
        '<slug:slug>/update_post',
        views.UpdatePost.as_view(),
        name='update_post'),
    path(
        '<slug:slug>/delete_post',
        views.DeletePost.as_view(),
        name='delete_post'),
    path(
        '<int:pk>/edit_comment',
        views.EditComment.as_view(),
        name='edit_comment'),
    path(
        'delete_comment/<int:pk>/',
        views.DeleteComment.as_view(),
        name='delete_comment'),
    # path(
    #     'delete_comment/<slug:post_slug>/<int:pk>/',
    #     views.DeleteComment.as_view(),
    #     name='delete_comment'),
]
