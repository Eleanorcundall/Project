from django.urls import path
from .views import home_view, blog_post_detail_view

urlpatterns = [
    path('', home_view, name='home'),
    path('blog/<slug:slug>/', blog_post_detail_view, name='blog_post_detail'),
]
