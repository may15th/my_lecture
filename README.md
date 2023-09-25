[TOC]
# 대제목 1
## 중제목 2
### 소제목 3

1. 순서 있는 리스트
2. 두 번째 요소
    1. 두번째의 자식요소
    2. 두번째의 두번째 자식요소
- 순서 없는 리스트
    1. 순서가 없는 리시트의 순서가 있는 자식 리스트
```python
print('hello world')
if true:
    print('hello world')
```
[naver](https://naver.com)
![이미지](https://picsum.photos/200/300)
**굵게**
*기울임*
~~취소선~~
___
**특수문자는 '-' '_' 2가지만 사용한다, 한글도 사용XX**
___
윈도 없을 때  dos 검은 바탕 흰글씨?
## CLI

### pdjango ORM with view
1. python manage.py makemigrations해도 변화 없음
   migrations 폴더안에 0001_initial.py 이미 있기 떄문.
   설계도는 이미 있다는 것. 최종적으로 db에 이 설계도를 전달해야 함.

2. python manage.py migrate
   0001_initial 기반으로 table이 하나 만들어질 거고 나머지 내장앱들이 작성된 설계도 기반으로 다른테이블 기반으로 만들어진다.
   (저번주 모델에 대한 내용)

### 2가지 조회 진행
3. read
   1. 전체 게시글 조회
    메인페이지에 게시글들 출력 해야함.
    조회를 어떻게 하는지 부터 진행.

    가. 전체 게시글들 조회를 위한 url부터 작성해야 함.
    지금 articles app의 urls.py를 보는데, crud의 urls.py를 보면
    (2개는 뭐가 다른거지...?)

    articles app - urls.py 에서 
    path('', views.)

    데이터 흐름에 따른 순서
    지금 내가 하고 있는과정은 app-articles에서
    url, views ... 을 차근차근 정보 주는 것.

    url -> view함수

    views에서 queryset api라는 문법을 통해서 데이터베이스에 전체 게시글에 대한 조회요청을 보낸다.
    그러면 그 결과가 queryset이라는 데이터로 오게 되고, 그거를 변수에 담아서 render 함수에 3번째 인자 context로 넘겨준다.


    1. model.objects.all() 이라는 queryset api문법 학습
        objects는 매니저라고 생각 고정이라고 생각. 뒤에 'all()'이부분이 갈아끼워지는 형태.


   2. 단일 게시글 조회


    python manage.py createsuperuser

    username : admmin
    email address : 공백
    pasword: admin1234(화면표시안됨)
    pasword(again): admin1234(화면표시안됨)
    빨간 에러문자 무시 y

    python manage.py runserver 한후 뒤에 /admin

    super계정을 만든이유는 게시글을 쓰기위함.

    별도로 커스텀한 모델클래스는 출력되고있지 않음.

    article(앱) 폴더의 admin.py에 여기서 등록을 해줬어야 됐음.

    article - admin.py에
    admin.site.register() 입력
    from .models import Article
    .(현재폴더) models에 있는 Article이라는 함수를 import한다. 

    admin 사이트 새로고침 하면 등장!

    admis 사이트에서 게시글 3개 작성

    메인페이지 주소/articles/로 가면 게시판 제목 ,1,2,3이 출력됨!

    index.html이 페이지 구조 짜는 곳이니깐
    여기서 
    <p>글 번호 : {{article.pk}}</p>
  <p>글 제목 : {{article.title}}</p>
  <p>글 내용 : {{article.content}}</p>
  <hr>
  위 입력 hr 태그는 구분선

  여기까지가 전체 게시글 조회

  이제 단일 게시글 조회

  variable routing이 라는 걸 하는데


  ==================================
2. CREATE
CREATE 로직 구현하기 위해 필요한 view 함수의 갯수는?

throw catch 기능 구현할 때도 같은 질문
사용자가 form 태그에 써서 다시 return받을 떄 두개

여기서도 2개 필요

 가. 사용자 입력 데이터를 받을 페이지를 렌더링 - new
 나. 사용자가 입력한 데이터를 DB에 저장 - create

언제나 url 먼저 작성 url도 2개가 나오겠지