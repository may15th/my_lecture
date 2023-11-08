from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.shortcuts import get_object_or_404, get_list_or_404
from .models import Article, Comment
from .serializers import ArticleListSerializer, ArticleSerializer, CommentSerializer


@api_view(['GET', 'POST'])
def article_list(request):
    if request.method == 'GET':
        # articles = Article.objects.all()
        # orm으로 전체 데이터달라 요청
        # 객체와 관계형 데이터베이스 매핑, 객체와db테이블이 매핑을 이루는 것.
        # 쿼리셋 형태로 데이터 받은 것. Article.objects.all() or get_list_or_404(Article)
        # 쿼리셋이란 - 전달받은 모델의 객체 목록. db로부터 데이터를 읽고, 필터를 걸거나 정렬
        # Model_name.objects.all()/get() 이런식의 문장 사용.
        articles = get_list_or_404(Article)
        # 이렇게 쿼리셋으로 받은 데이터를 그대로 사용하는게 아니라 
        # 시리얼라이저라는 변환기를 통해서 결과물 만들어낸 다음에
        serializer = ArticleListSerializer(articles, many=True)
        # 결과물만 추출하는 .data를 통해서 리스폰스한다.
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'DELETE', 'PUT'])
def article_detail(request, article_pk):
    # article = Article.objects.get(pk=article_pk)
    article = get_object_or_404(Article, pk=article_pk)

    if request.method == 'GET':
        serializer = ArticleSerializer(article)
        return Response(serializer.data)

    elif request.method == 'DELETE':
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    # 쟝고 템플릿과 다른 부분
    # 일반적인 장고 수정과 다른 부분은 내용만 수정, 제목만 수정 할 수 있어.
    # 수정할 필드만 추가로 데이터 보낸다.
    # 근데 여기서는 둘 다 같이 데이터 보내줘야 한다. title만 수정하고 싶어도
    # content도 같이 보내줘야 한다는 것.

    # 걸린 부분이 .is_valid에서 걸린 것.
    # content field가 빈 요청이 들어온 것.
    # 아티클시리얼라이저가 아티클 객체를 인스턴스로 받고 data를 데이터로 받아서 시리얼 라이저 만드는데
    # 아티클 시리얼라이저의 기본값으로 partial이 있는데, 이게 title, field 중 하나만 수정 가능ㅎ다로고
    # 해주는 것. 기본값이 false라서 partial = True로 해주면 잘 됨.

    elif request.method == 'PUT':
        serializer = ArticleSerializer(article, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# json 파일은 데이터 타입이 하나의 큰 문자열이다.
# 이거를 파이썬에서 쓸 수있는 타입으로 변환해서 사용하는 것
# comments.json으로 loaddata한 건 무슨 의미가 있는 거지?
@api_view(['GET'])
def comment_list(request):
    comments = Comment.objects.all()
    # 다중데이터 (전체 조회니깐) many=True가 기본값이라고 생각.
    serializer = CommentSerializer(comments, many=True)
    return Response(serializer.data)


@api_view(['GET','DELETE','PUT'])
def comment_detail(request, comment_pk):
    # 단일댓글이니깐 변수명도 's'뺀 테이블에서 pk = comment_pk인 comment불러오는 queryset
    comment = Comment.objects.get(pk=comment_pk)
    # 다중데이터 (전체 조회니깐) many=True가 기본값이라고 생각.
    if request.method == 'GET':
        serializer = CommentSerializer(comment)
        return Response(serializer.data)
    
    # 삭제는 항상 쉬웠음. 위에서 쿼리셋으로 comment변수 정의해줬고
    # comment.delete()로 삭제해주는 것 뿐.
    # return은 204상태값 반환해주고 끝!
    elif request.method == 'DELETE':
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'PUT':
        # 댓글에 partial이 필요할까? 댓글은 일부러 입력들어온 데이터가 content밖에 없어.
        # article은 외래키가 직접 입력하는 게 아니야. 
        # article 작성할 떄는 title, content중에 하나만 수정할 때, title을 read_only_fields로지정해준 것.
        # put이라고 무조건 partial옵션 들어가는 것 아니야.
        serializer = CommentSerializer(comment, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        

@api_view(['POST'])
def comment_create(request, article_pk):
    # comment_create과정이지만 변수명도 article로 하고, Article모델에서 일치pk찾아서
    # 정보 담아오는 queryset 사용
    # 일치하는 데이터를 불러오는 과정
    article = Article.objects.get(pk=article_pk)
    # 이 부분이 다른 view함수랑 다르고 특이한데, article을 시리얼라이저에서
    # 바로 사용하지 않고 request.data 요청객체의 데이터를 담은 데이터를 인자로 한
    # Comment serializer 사용
    serializer = CommentSerializer(data=request.data)
    # raiese_exception 의 디폴트는 False인데, 트루로하면 유효성검사에서 문제가
    # 발생했을 때 굳이 어떤 조치 취하지 않아도, bad request 띄워준다.
    # 그러니깐 return Response(serializer.error, status = status.400 badrequest)이걸르 ㄹ
    # 굳이 쳐줄 필요 없다는 얘기
    if serializer.is_valid(raise_exception = True):
        # article은 왜 누락 됐을까?
        # 모델폼의 구조였다면?
        # 바로 save하지 않고 잠시 보류 했었다. 
        # serializer.save(commit=False)이렇게 그리고 인스턴스를 생성해줬어.
        # comment = serializer.save(commit=False)
        # 인스턴스만 생성하고 실제 저장요청은 보내고 있지 않은 상황. 이후
        # comment.article = article
        # serializer.save() 이런 식.
        # drf 개발자들이 template 구성과 유사하게 구성했을 뿐 100% 같은 메서드 아니라는 점 기억.
        # 모델 시리얼라이저에는 commit이라는 키워드 없어.
        # 누락 되어있는 필드 값에 아티클클래스를 넣어줘.*******
        # drf는 입력받아야 하는 모든 필드 다 조사.
        # article필드 required 하다는 메시지 ....
        # serializer.save(article=article)로 데이터 넣어준 건 맞는데, 데이터 입력전에 is_valid검사가 이루어졌어.
        # 1.댓글이 만들어졌을 때 조회는 가능하면서 2.유효성검사는 제외시켜야 한다
        # 이런 필드를 '읽기전용필드'라고 한다. 옵션이 필요 시리얼라이저 클래스에서 read_only_fields를 설정해준다.
        serializer.save(article=article)
        # 성공했을 때 생성 성공한 새로 만들어진 데이터를 리턴하고, 
        return Response(serializer.data, status=status.HTTP_201_CREATED)
        # 결국 article create랑 비슷한데, comment테이블에 article이라는 외래키 필드를 넣어줬고
        # 이 article이라는 외래키 필드로 어떻게 이후 조작하냐의 문제.
        
        #DELETE&PUT은 아티클이라고 써져있는 부분을 COMMENT라고 바꾸기만 해도 되는 부분이야.



        # get_object_or_404()
        # 모델 manager objects에서 get()을 호출하지만, 해당 객체가 없을 땐
        # 기존 DoesNotExist 예외 대신 http404를 raise함.
        # 사용자가 찾고자 하는 게 없을 떄 서버가 꺼지면, 다른 사용자들은?
        # 이렇게 찾고자 하는 해당 객체가 없을 tryexcept로 예외처리하는 게 아니라
        # 한줄로 쓰자는 것.
        # 500error가 뜨면 server측 에러라고 뜬다고 함.
        # 사실 이건 client의 잘못임 왜냐면 client가 없는 객체를 요청했기 때문
        # 그러니깐 우리는 404라고 너가 찾는 건 내가 가지고 있지 않아라고 정확히 말해줘야 함.

        # article = Article.objects.get(pk=article_pk)
        # articles = Article.objects.all()
        # comment = Comment.objects.get(pk=article_pk)
        # 처럼 작성된 것들을
        # article = get_object_or_404(Article)
        # articles = get_object_list_404(Article)
        # comment = get_object_or_404(Comment)
        # 이런 식으로 작성하는 것!!!

    # get_list_or_404, get_object_or_404는 api개발할 때 적합한 메서드
