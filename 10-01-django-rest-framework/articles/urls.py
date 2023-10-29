from django.urls import path
from articles import views


urlpatterns = [
    path('articles/',views.article_list),
    # path('articles/<int:')
    path('articles/<int:article_pk>/', views.article_detail)

    # path('articles/create/') 이런식으로 만들 필요가 없다. 이후 views에서 분기처리해서 만들면 됨.
    # rest 관점에서 봤을 때 url을 식별 용도로만 사용한다. 위치를 추상화. 'articles/create/'는 만들다는 행위의 의미가 담겨있음.
    # rest에서는 행위를 request method로 표현하기로 약속했어.
    # 요청을 post로 보내 이렇게 명확하게 나눈 것.
    
]
