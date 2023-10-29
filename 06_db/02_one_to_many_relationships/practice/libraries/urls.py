from django.urls import path
from . import views

# app_name 구분하는 이유도, 경로가 복잡해질 수록, 나눠서 부르는게 맞다.
app_name = 'libraries'
urlpatterns = [
    # 사용자의 요청에 맞는 음답을 해줄 것 -> 그 응답 : 코드가 한다. (어떤 일을 하는것 -> 함수)
    # Web 개발의 desugn pattern으로 나눠보니 Model, View, Template
    path('authors/',  views.authors, name='authors'),
    path('authors/<int:author_pk>/',  views.detail, name='detail'),
    path('<int:author_pk>/books/create/',  views.book_create, name='book_create')
]
