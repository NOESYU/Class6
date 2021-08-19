from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from projectapp.models import Project

# 구독 시스템은 연결된 정보가 하나만 있어야함 !
class Subscription(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             related_name='subscription', null=False)
    project = models.ForeignKey(Project, on_delete=models.CASCADE,
                                related_name='subscription', null=False)

    class Meta: # 이 유니크가 연결을 하나만 하게끔 해줌!
        unique_together = ['user', 'project']
