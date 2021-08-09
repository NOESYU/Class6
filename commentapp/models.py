from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from articleapp.models import Article


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.SET_NULL,
                                related_name='comment', null=True) # 본문(아티클)
    writer = models.ForeignKey(User, on_delete=models.SET_NULL,
                               related_name='comment', null=True) # 작성자
    content = models.TextField(null=False) # 내용
    created_at = models.DateTimeField(auto_now_add=True) # 게시힌 날짜