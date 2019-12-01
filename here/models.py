from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=100, verbose_name="제목")
    user_name = models.CharField(max_length=100, blank=True,
                                 choices=[1,2,3,4,5,"고양이"])
    lnt_lng = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


# Create your models here.
