from django.urls import path
from .views import home_view, blog_post_detail_view, category_view, like_post


urlpatterns = [
    path('', home_view, name='home'),
    path('blog/<slug:slug>/', blog_post_detail_view, name='blog_post_detail'),
    path('category/<str:category>/', category_view, name='category_posts'),
    path('like/<int:post_id>/', like_post, name='like_post'),
]
