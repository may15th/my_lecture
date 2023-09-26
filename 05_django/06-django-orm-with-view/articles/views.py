from django.shortcuts import render
from .models import Article

# article은 import를 해와야 사용할 수 있따.
# 같은 위치에 있기 때문에
# Create your views here.

# 전체 조회 .all()메서드 사용함 확인.
def index(request):
    # 모델.objects.all() 이라는 형식인데
    # Article = 모델임
    articles = Article.objects.all()

    context = {
        'articles' : articles,

    }
    return render(request, 'articles/index.html', context)
    # context 딕셔너리 파일에 이 데이터가 들어가게 된다.
    # request는 그냥 쓰는 거고, 'articles/index.html이 템플릿 경로, context가?
    # all()메서드의 특징은 전체 게시글 조회 게시글 하나이상이거나 상관없이 쿼리셋으로 리턴해줌.
    # 리턴해준 결과를 articles라는 변수에 담는다.

def detail(request, pk):
    article = Article.objects.get(pk=pk)   #get()메서드의 특징: 찾고 나서의 결과가 두 개 이상이면 error, 찾았는데 없을때도 error가 난다!
    context = {
        'article' : article,
        }                        
                            # 딱 하나만 있을 때 다른것들과 겹치지 않게 조회하기 위해 제목, 내용보다는 각 데이터의 유일한 식별자인 pk를 사용
                            # 왼쪽의 pk는 컬럼명인 pk이고 오른쪽의 pk는 variable routing을 통해 온 변수의 이름.
    return render(request, 'articles/detail.html', context)

# new함수는 진짜 new.html만 불러오면 됌.
def new(request):
    return render(request, 'articles/new.html')

def create(request):
    title = request.GET.get('title')
    content = rquest.GET.get('content')

    #1

    # 게시글을 저장하는 3가지 방식
    # 1. 인스턴스 만들어서 데이터를 하나씩 넣는 방식.
    # article = Article()
    # article.title = title
    # article.content = content
    # # 위 request.GET 까지가 딕셔너리 .get메서드의 빈 속성 이게 new.html의 name 속성의 title, content
    # article.save()
    # db에 레코드 한 줄 작성하려면 save()메서드가 호출이 되야 한다.

    # 인스턴스 클래스의 정의를 통해 만들어진 객체를 의미
    # ex) oop(객체지향 프로그래밍)에서 클래스에 소속된 개별적인 객체
    # 예를 들어, 사용자(user)라는 클래스를 정의하고 홍길동(hong)이라는 객체를
    # 생성할 경우, hong이라는 객체는 user라는 클래스의 인스턴스가 된다.





    # 2. 초기값으로 애초에 인스턴스를 만드는 방법.

    # !!!!!!!!!!!이 방법을 사용!!!!!!!!!!!!!!!

    article = Article(title=title, content=content)
    article.save()

    # 유효성 검사가 목적.


    return(request, 'articles/create.html')












    # 3. quarysetAPI에 createmethod를 활용하는 방법

    # qierysetapi란 무엇인가?

    # ORM(Object-Relational-Mapping)
    # 객체와 관계형 db 데이터를 매핑 해주는 것. -> 하나의 값을 다른 값으로 대응시키는 것.
    # 객체간의 관계를 바탕으로 SQL을 자동 생성하여 sql 쿼리문 없이도 db의 데이터베이스
    # 데이터를 다룰 수 있게 해준다.

    # Article.objects.create(title=title, content=content)

    # 

