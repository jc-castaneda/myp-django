from django.db import models
from users.models import CustomUser

# Creating model for a Post
class Post(models.Model):
    # Post's metadata
    title = models.CharField(max_length=255)
    description = models.TextField()
    creator = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='created_posts')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    likes = models.ManyToManyField(CustomUser, related_name='liked_posts', blank=True)

    # Defines Post's status
    status = models.CharField(max_length=20, choices=[
        ('OPEN','open'),
        ('IN_PROGRESS', 'In Progress'),
        ('COMPLETED', 'Completed')
    ], default='OPEN')

    # Post's tags
    genre = models.CharField(max_length=100, blank=True)
    looking_for = models.CharField(max_length=50, blank=True)


# Creating model for a Comment
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
