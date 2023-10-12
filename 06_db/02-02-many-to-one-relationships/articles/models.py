from django.db import models
from accounts.models import User
from django.conf import settings

# models.py 에서는 문자열을 참고핟로록 권장함. 그래서2,3라인 import 후 9번 라인 AUTH_USER_MODEL
# models.py아닌 form같은 데서 참조할 떄는 get_user_model() User 객체 참조.

# Create your models here.
class Article(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=10)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

