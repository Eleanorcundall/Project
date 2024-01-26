from django.urls import path
from .views import home_feed_view

urlpatterns = [
    path('', test, name='home_feed'),
]