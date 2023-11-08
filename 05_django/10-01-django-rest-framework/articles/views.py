from rest_framework.response import Response
from .models import Article
from .serializers import ArticleListSerializer, ArticleSerializer
from rest_framework.decorators import api_view
from rest_framework import status

# Assertion Error
# DRF에는 한 가지 약속이 있는데, 반드시 데코레이터를 붙여야 한다는 약속
# 필수다!!! 아니면 DRF 함수가 작동하지 않는다.
# from rest_framework.decorators import api_view 이거 임포트 받은 후에

@api_view(['GET', 'POST'])
def article_list(request):
    articles = Article.objects.all()
    if request.method == 'GET':
        # 게시글 전체 조회 한 다음에 어떤 변환기에 의해 변환해주고
        # 변환한 것을 리턴 하는 것.``
        # articles를 전체 조회할 건데 모델이 ~필요하겠지.
        # 예전에는 이걸 context담아서 render쪽에 보냈다면
        # 지금은 template띄울 필요 없기 때문에
        # serializer라는 새로운 결과물로 바꾸는 것.`
        # 쟝고 서버는 더이상 파이썬 언어로만 응답하는 게 아니라 다양한 언어(json)으로 반환 할 수 있도록 유연한 데이터로 변환 때문
        # 위까지는 똑같은 데이터 확인한 게 맞음. 템플릿 렌더하던 떄랑 똑같은.
        serializer = ArticleListSerializer(articles, many=True)
        # 그냥 반환하는 게 아니라 render함수처럼 drf에서 제공하는 response라는 함수사용 한다.``~
        # 그리고 그냥 serializer넣어주는 게 아니라 serializer.data로 써줘야 한다.
        # 그 이유는 serializer는 그냥 객체일뿐인데, RESPONSE의 객체로는 JSON형식이 필요하다.
        # JSON 형식은 큰 리스안에 작은 딕셔너리가 들어간 구조인데, 이련 형식으로 변환해주는 게 .data 메서드이다.
        
        return Response(serializer.data)

    # else는 잘 안 쓰고 elif를 쓰는데, 그 이유는 명시성이 떨어지기 때문.
    # 나중에 put, delete도 넣을 건데, 마지막을 else로 넣으면 그게 어떤 메서드인지 알기 어렵다!
    # 아래가 이전 구성이었다. 수정할 경우 수정된 아티클 폼 이용해서 form인스턴스 만들고, 유효성 검사 진행
    # elif request.method == 'POST':
    #     form  = ArticleForm(request.POST)
    #     if from.is_valid
    elif request.method == 'POST':
        #데이터 받는게 아티클 폼이 아니라 아티믈 시리얼라이저로 변한 것!
        # 아티클시리얼라이저라는 클래스가 데이터라는 인스턴스 객체만을 받기 떄문에
        # form =ArticleForm(request.POST)로 정보 받던 템플릿 부분이랑은 조금 다르다!
        # is_valid()라는 유효성 검사 메서드 사용하는데 이건 템플릿 부분이랑 이름만 똑같지 시리얼라이저의
        # 데이터 검사한다는 점에서 다른 메서드임.
        serializer = ArticleSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            # 유효성 검사 통과한다면 201 코드 띄우고
            # 리스폰스에 첫번째로 오는 인자는 데이터라서 serializer.data로 시리얼라이저의 데이터 부분을 넣어주고
            # 유효성 검사 성공하면 201 실패하면 400? 띄워야 되는데 그런 상태 코드를 drf가 미리 만들어놔서 그거 임포트 시켜줌.
            # from rest_framework import status 이를 임포트 시켜주면 됌. status 안에 여러가지 class가 존재하는 것.
            # RESPONSE 클래스는 1,2번째 인자로 data, status 인스턴스를 인자로 받으므로 아래와 같이 처리해 줌.
            return Response(serializer.data, status = status.HTTP_201_CREATED)
            # 생성한 결과물도 serializer.data로 저장 되는 것.
        #유효성 검사 실패한다면
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# 과거 방식
# def index(request):
#     articles = Article.objects.all()
#     context = {
#         'articles':articles,
#     }
#     return render(request, 'articles/index.html', context)`
# DELETE는 베리어블 라우팅 - 몇 번째 게시글인지 조회해야해서 여기에 생성
@api_view(['GET','DELETE', 'PUT'])
def article_detail(request, article_pk):
    # 위에서는 Article모델에서 데,이터 담는 변수명을 article's'로 했는데 여기는 article 특정 pk와 일치하는 것 만 호출 하기 떄문.
    # article_pk와 일치하는 하나의 정보만 들고 올때는 .all이 아니라 .get을 사용한단거 기억하자 ㅋㅋㅋㅋ
    article = Article.objects.get(pk=article_pk)
    if request.method == 'GET':
        #위랑 똑같이 context사용 안하고 serializer 변환기 한` 번 돌린다고 생각.
        serializer = ArticleSerializer(article)
        return Response(serializer.data)

    elif request.method == 'DELETE':
        # delete메서드는 따로 serialize하지 않는다. 그냥 지우기만 하는거니까
        # 템플릿 할때처럼 간단하게 article.delete()하고 리스폰스 받아오면 끝.
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        # delete 실행할 경우 응답 데이터 오는 것은 없는데
        # 관련된 걸 어떻게 표현할지 코드 안쳤기 때문에.
        # 그래도 상태창에 204가 뜰 것.
    # put 수정은 crud때처럼 생각할 게 한 두 가`지 있어
    # 기존에 썼던 update와 차이점 
    
    elif request.method == 'PUT':
        # 템플릿 할때
        # form = ArticleForm(request.POST, instance=article)

        # api할 떄는 이렇게 instance인 article이 앞으로 오고, request.POST대신에
        # request.data가 두번째로 간닷!
        serializer = ArticleSerializer(article, request.data)
        if serializer.is_valid():
            serializer.save()
            # 수정완료 status는 200을 주는데, 이건 기본 값으로 줘서 굳이 status = status.200
            # 을 두번째 인자로 줄 필요 x
            # 이건 저장이 성공했을 때
            return Response(serializer.data)
        #저장이 실패했을 때는 post랑 똑가티 에러 메시지 400
        return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)