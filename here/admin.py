from django.contrib import admin
from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'cat', 'title', 'user_name', 'lnt_lng', 'created_at', 'updated_at']
    list_per_page = 10


# Register your models here