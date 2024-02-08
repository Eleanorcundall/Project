from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from content_feeds.models import Like

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    favorite_products = models.TextField(blank=True)
    profile_picture = CloudinaryField('image', default='placeholder')
    likes_received = models.IntegerField(default=0)
    likes_given = models.ManyToManyField(Like, related_name='liked_by', blank=True)

    def __str__(self):
        return self.user.username
