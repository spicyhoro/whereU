from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=100)
    user_name = models.CharField(max_length=100, blank=True)
    lnt_lng = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


# Create your models here.
