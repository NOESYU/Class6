from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from projectapp.models import Project


class Article(models.Model):
    writer = models.ForeignKey(User, on_delete=models.SET_NULL,
                               related_name='article', null=True)
    # 프로젝트(게시판)와 아티클 연결용
    # null 은 디비에 비어있어도 된다는 느낌, blank 는 ㄹㅇ 개시할때 입력안해도 되는 것!
    project = models.ForeignKey(Project, on_delete=models.SET_NULL,
                                related_name='article', null=True, blank=True)
    title = models.CharField(max_length=200, null=True)
    image = models.ImageField(upload_to='article/', null=True)
    content = models.TextField(null=True)

    created_at = models.DateField(auto_now_add=True)

    # 좋아요 필드
    like = models.IntegerField(default=0)