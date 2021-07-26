from django.contrib.auth.models import User
from django.db import models

# Create your models here.
# 프로필 모델 : 이미지, 닉네임, 메시지 3개!
# 프로필앱은 1:1로 어카운트앱과 연결 시켜주기!! 프로필 앱 자체에는 딜리트XX
class Profile(models.Model):
    # 유저 클래스와 연결, 옵션 - 연쇄삭제, 접근할수있게 profile 설정
    user = models.OneToOneField(User, on_delete=models.CASCADE,
                                related_name='profile')

    image = models.ImageField(upload_to='profile/', null=True)
    nickname = models.CharField(max_length=30, unique=True, null=True)
    message = models.CharField(max_length=200, null=True)

    # 모델 작성하고 migration 해주기!! makemigrations(init파일생성), migrate(디비에저장)