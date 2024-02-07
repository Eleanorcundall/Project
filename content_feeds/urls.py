from django.urls import path
from .views import home_view, blog_post_detail_view, category_view


urlpatterns = [
    path('', home_view, name='home'),
    path('blog/<slug:slug>/', blog_post_detail_view, name='blog_post_detail'),
    path('category/<str:category>/', category_view, name='category_posts'),
]
