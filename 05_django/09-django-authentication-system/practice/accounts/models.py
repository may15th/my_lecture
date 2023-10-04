from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    score = models.IntegerField(default=100)

    # models.py에 user class만 정의하면 되느냐?

    
