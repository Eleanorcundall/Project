from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
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


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    post = GenericForeignKey('content_type', 'object_id')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['user', 'content_type', 'object_id'], name='unique_like')
        ]

        def __str__(self):
            return f"{self.user} likes {self.post}"