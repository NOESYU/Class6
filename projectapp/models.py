from django.db import models

# Create your models here.


class Project(models.Model):
    name = models.CharField(max_length=20, null=False)
    description = models.CharField(max_length=200, null=True)
    image = models.ImageField(upload_to='project/', null=False)
    created_at = models.DateTimeField(auto_now_add=True)


    # DB를 바꾸는게 아니니까 migrations 할 필요 없음!
    def __str__(self): # 프로젝트 객체 출력될때 글(이름) 출력되는거 설정
        return f'{self.name}'