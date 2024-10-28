from django.urls import path
from .views import home_view, blog_post_detail_view, category_view, like_post, comment_on_post, edit_comment, delete_comment
from user_submissions.views import submit_post, delete_post

urlpatterns = [
    path('', home_view, name='home'),
    path('blog/<slug:slug>/', blog_post_detail_view, name='blog_post_detail'),
    path('category/<str:category>/', category_view, name='category_posts'),
    path('delete/<slug:slug>/', delete_post, name='delete_post'),
    path('edit/<slug:slug>/', submit_post, name='edit_post'),
    path('like/<int:post_id>/', like_post, name='like_post'),
    path('comment/<int:post_id>/', comment_on_post, name='comment_on_post'),
    path('edit-comment/<int:comment_id>/', edit_comment, name='edit_comment'),
    path('comment/delete/<int:comment_id>/', delete_comment, name='delete_comment'),
    
]
