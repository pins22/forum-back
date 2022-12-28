from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=1024)
    body = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    last_changed = models.DateTimeField(blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    points = models.IntegerField(default=0)
    upvotes = models.ManyToManyField(User, related_name="upvotes", blank=True)
    downvotes = models.ManyToManyField(User, related_name="downvotes", blank=True)

    def __str__(self):
        return "Post: " + self.title


class Reply(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    last_changed = models.DateTimeField(blank=True, null=True)
    points = models.IntegerField(default=0)

    def __str__(self):
        return "Reply: " + self.body
