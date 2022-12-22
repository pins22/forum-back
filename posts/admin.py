from django.contrib import admin

from posts.models import Post, Reply

# Register your models here.

admin.site.register(Post)
admin.site.register(Reply)
