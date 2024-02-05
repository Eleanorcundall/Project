from django.db import models
from django.contrib.auth.models import User
from autoslug import AutoSlugField 
from cloudinary.models import CloudinaryField


class BlogPost(models.Model):
    CATEGORY_CHOICES = [
        ('Hair', 'Hair'),
        ('Skin', 'Skin'),
        ('Sexual Wellness', 'Sexual Wellness'),
        ('Menstrual Wellness', 'Menstrual Wellness'),
        
    ]

    STATUS_CHOICES = [
        ('draft', 'Draft'),
        ('published', 'Published'),
        ('archived', 'Archived'),
    ]

    title = models.CharField(max_length=200)
    content = models.TextField()
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    created_at = models.DateTimeField(auto_now_add=True)
    featured_image = CloudinaryField('image', default='placeholder')
    slug = AutoSlugField(populate_from='title', unique=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='draft')
    

    def __str__(self):
        return self.title
