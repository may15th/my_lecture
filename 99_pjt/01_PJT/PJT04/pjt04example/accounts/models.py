from django.db import models
from django.contrib.auth.models import AbstractUser

# django가 기본적으로 user 모델을 가지고 있는데 
# 왜 덮어씀?
# 1. django의 권장사항
# 2. custom하기 위해서
class User(AbstractUser):
    # 내가 원하는 추가적인 필드를 사용
    nickname = models.CharField(max_length=30)
