from django.urls import path
from . import views

# app_name 구분하는 이유도 경록가 복잡해질 수록 나누어 부르는 게 좋다.
app_name = 'libraries'
urlpatterns = [
    # 사용자의 요청에 맞는 응답을 해줄 것. -> 그 응답: 코드가 한다. (어떤 일을 하는 것 -> 함수)
    path('authors/', views.authors, name='authors'),
    path('authors/<int:author_pk>', views.authors, name='detail'),
    # path('authors/<int:author_id>/', views.author_detail, name='author_detail'),
    path('<int:author_pk>')
]
