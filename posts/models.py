from django.db import models

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=1024)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    last_changed = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return "Post: " + self.title


class Reply(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    last_changed = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return "Reply: " + self.body
