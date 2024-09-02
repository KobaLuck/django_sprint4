from django.urls import path

from .views import (
    EditPostView, DeletePostView, AddCommentView,
    IndexListView, UserProfileView, EditUserProfileView,
    PostDetailView, PostCreateView, CategoryListView,
    EditCommentView, DeleteCommentView
)


app_name = 'blog'


urlpatterns = [
    path(
        'posts/<int:post_id>/',
        PostDetailView.as_view(),
        name='post_detail'
    ),
    path(
        'category/<slug:category_slug>/',
        CategoryListView.as_view(),
        name='category_posts'
    ),
    path(
        '',
        IndexListView.as_view(),
        name='index'
    ),
    path(
        'posts/create/',
        PostCreateView.as_view(),
        name='create_post'
    ),
    path(
        'posts/<int:post_id>/edit/',
        EditPostView.as_view(),
        name='edit_post'
    ),
    path(
        'edit_profile/',
        EditUserProfileView.as_view(),
        name='edit_profile'
    ),
    path(
        'posts/<int:post_id>/delete/',
        DeletePostView.as_view(),
        name='delete_post'
    ),
    path(
        'profile/<str:username>/',
        UserProfileView.as_view(),
        name='profile'
    ),
    path(
        'posts/<int:post_id>/comment/',
        AddCommentView.as_view(),
        name='add_comment'
    ),
    path(
        'posts/<int:post_id>/delete_comment/<int:comment_id>/',
        DeleteCommentView.as_view(),
        name='delete_comment'
    ),
    path(
        'posts/<int:post_id>/edit_comment/<int:comment_id>/',
        EditCommentView.as_view(),
        name='edit_comment'
    ),

]
