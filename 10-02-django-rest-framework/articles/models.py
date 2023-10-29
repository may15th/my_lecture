from django.db import models


# Create your models here.
class Article(models.Model):
    # vachar은 CharField로 입력.
    title = models.CharField(max_length=10)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

# article과 N:1관계이고 외래키를 가지는 테이블은 n쪽임.
# article=comment중에 n쪽은 comment인데 그 이유는
# article 하나에 0개 이상의 comment가 달리기 때문.
class Comment(models.Model):
    # 외래키는 참조테이블의 소문자 단수형을 쓰기로 했고.
    # 포링키 인자는(to = 참조테이블, delete 옵션)
    article = models.ForeignKey(Article,on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

