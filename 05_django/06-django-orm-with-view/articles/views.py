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
    # 게시글을 저장하는 3가지 방식
    # 1. 인스턴스 만들어서 데이터를 하나씩 넣는 방식.
    article = Article()
    article.title = request.GET.get('')