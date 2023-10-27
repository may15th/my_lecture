from rest_framework.response import Response
from .models import Article
from .serializers import ArticleListSerializer, ArticleSerializer
from rest_framework.decorators import api_view

# Assertion Error
# DRF에는 한 가지 약속이 있는데, 반드시 데코레이터를 붙여야 한다는 약속
# 필수다!!! 아니면 DRF 함수가 작동하지 않는다.
# from rest_framework.decorators import api_view 이거 임포트 받은 후에

@api_view(['GET'])
def article_list(request):
    # 게시글 전체 조회 한 다음에 어떤 변환기에 의해 변환해주고
    # 변환한 것을 리턴 하는 것.
    # articles를 전체 조회할 건데 모델이 필요하겠지.
    articles = Article.objects.all()
    # 예전에는 이걸 context담아서 render쪽에 보냈다면
    # 지금은 template띄울 필요 없기 때문에
    # serializer라는 새로운 결과물로 바꾸는 것.
    # 쟝고 서버는 더이상 파이썬 언어로만 응답하는 게 아니라 다양한 언어(json)으로 반환 할 수 있도록 유연한 데이터로 변환 때문
    # 위까지는 똑같은 데이터 확인한 게 맞음. 템플릿 렌더하던 떄랑 똑같은.
    
    serializer = ArticleListSerializer(articles, many=True)
    # 그냥 반환하는 게 아니라 render함수처럼 drf에서 제공하는 response라는 함수사용 한다.
    # 그리고 그냥 serializer넣어주는 게 아니라 serializer.data로 써줘야 한다.
    # 그 이유는 serializer는 그냥 객체일뿐인데, RESPONSE의 객체로는 JSON형식이 필요하다.
    # JSON 형식은 큰 리스안에 작은 딕셔너리가 들어간 구조인데, 이련 형식으로 변환해주는 게 .data 메서드이다.
    
    return Response(serializer.data)

# 과거 방식
# def index(request):
#     articles = Article.objects.all()
#     context = {
#         'articles':articles,
#     }
#     return render(request, 'articles/index.html', context)

@api_view(['GET', 'POST'])
def article_detail(request, article_pk):
    if request.method == 'GET':
        articles = Article.objects.all(pk=article_pk)
        #위랑 똑같이 context사용 안하고 serializer 변환기 한 번 돌린다고 생각.
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':