from django.db import models

# Create your models here.
# 단순히 선으로 그리는 게 아니라 erd라는 걸 그린다...
# 모델관계들을 그리는 것.
# db정의하는 방법 원래는 sql사용한다.
# sql없이 어떻게 table을 정의할 수 있나?
# python class로 정의한다.

class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True) # 날짜만 넣을지, 시간만 넣을지, 모두 넣을지 선택 autonowadd = true 데이터 한줄 추가되는 순간 시간 '한번만' 자동 입력
    updated_at = models.DateTimeField(auto_now=True)    # 수정될 때마다 계속 기록
    
    # 이주 계획서 설계도가 필요하다. 어차피 프로젝트니깐 manage
    # 클라이언트가 서버에 요청을 보낸다. 전체 게시글 조회요청 get. article어쩌고
    # 원래 경로는 project폴더에urls.py였음. 
    # 이제는 모든 경로를 app마다 분리해서 관리할 것.
    