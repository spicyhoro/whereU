from django.db import models


class Post(models.Model):
    STATUS_CHOICES = (
        ('h', 'horo'),
        ('l', 'lolens'),
        ('s', 'spicyhoro'),
    )


    title = models.CharField(max_length=100, verbose_name="제목")
    user_name = models.CharField(max_length=100, blank=True,
                                 choices=STATUS_CHOICES, verbose_name="유저이름")
    cat = models.CharField(max_length=100, blank=True, verbose_name="고양이")
    lnt_lng = models.CharField(max_length=100, verbose_name="위치")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="만든날짜")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="최근수정날짜")


# Create your models here.
