from django.db import models
#어떻게 클래스처럼 접근 가능한가? __init__.py가 그 역할 해주는 것.
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    pass
