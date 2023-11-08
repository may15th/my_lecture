from django.urls import path
from articles import views


urlpatterns = [
    path('articles/', views.article_list),
    path('articles/<int:article_pk>/', views.article_detail),
    # 전체 댓글 조회get
    path('comments/', views.comment_list),
    # 단일 댓글 get, put 
    path('comments/<int:comment_pk>/', views.comment_detail),
    # 댓글 생성 post
    # url에서 행위에 대한 정보가 나오는 건 rest에서 좋지 않다 create하자는 건 호스트 method로 표현을 한다.
    path('articles/<int:article_pk>/comments/', views.comment_create),
]
# 댓글 데이터를 json데이터로 보내줘야 하는데, queryset으로 데이터가 올 것.
# 이 쿼리셋을 그대로 json으로 변경할 수는 없어.
# 이 데이터를 유연하게 다른 데이터 타입으로 유연한 데이터로 만드는 과정 그게 
# 시리얼라이제이션, 그리고 시리얼라이저 클래스들이 그 변환기 쟝고에서 만든 데이터 타입을
# 다른 데이터로 언제든지 변화시키는 중간정도 데이터타입으로 만들어주는 것.
