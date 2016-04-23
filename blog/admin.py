from django.contrib import admin
# Import the blog posts
from .models import Post

# Register your models here.
admin.site.register(Post)
