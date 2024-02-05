from django.urls import path
from .views import submit_post

app_name = 'user_submissions'

urlpatterns = [
    path('submit/', submit_post, name='submit_post'),
]