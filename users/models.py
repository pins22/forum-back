from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class UserProfile(models.Model):
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)

    def __str__(self):
        return "Profile for " + self.user.username


class User(AbstractUser):
    profile = models.ForeignKey(
        UserProfile, on_delete=models.CASCADE, blank=True, null=True)
