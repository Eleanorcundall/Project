from django.db import models
from django.contrib.auth.models import User
from autoslug import AutoSlugField 
from cloudinary.models import CloudinaryField

class UserSubmission(models.Model):
    STATUS_CHOICES = [
        ('draft', 'Draft'),
        ('published', 'Published'),
    ]

    CATEGORY_CHOICES = [
        ('Hair', 'Hair'),
        ('Skin', 'Skin'),
        ('Sexual Wellness', 'Sexual Wellness'),
        ('Menstrual Wellness', 'Menstrual Wellness'),
    ]

    title = models.CharField(max_length=255)
    content = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
    slug = AutoSlugField(populate_from='title', unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, null=True, blank=True)
    featured_image = CloudinaryField('image', default='placeholder')
    

    def __str__(self):
        return self.title