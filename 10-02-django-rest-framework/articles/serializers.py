from rest_framework import serializers
from .models import Article, Comment


class ArticleListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('id', 'title', 'content',)


class CommentSerializer(serializers.ModelSerializer):
    class ArticleSerializer(serializers.ModelSerializer):
        class Meta:
            model = Article
            fields = ('title',)

    # override
    article = ArticleSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = '__all__'
        # read_only_fields = ('article',)

# 결과물 출력이 왔다는 건 무조건 validation이 진행 됐다는 것.
# put에서 진행되는 시리얼라이저가 is_valid에서 title,content 둘다 확인 한다는 것.
# drf는 기본적으로 'all이라면 유효성 검사 진행.
# 수정에서 원하는 건 일부 데이터 수정
# 전체 데이터 수정 항상 원하지 않아.

class ArticleSerializer(serializers.ModelSerializer):
    # 역참조의 매니저 이름은 역참조할 모델명_set으로 정해져있어.
    # comment데이터를 json으로 직렬화 하기 위해서는 시리얼라이제이션 필요
    # 1->N쪽참조하는 것. 댓글이 0개이건 1개이건 다중데이터가 나오는 것. 
    # 다중데이터에 대한 옵션을 넣어줘야 함 many=True
    # 이 필드를 읽기전용으로 안바꾸면, 기존 아티클에 문제 발생
    # comment_set을 활성화시켰기 떄문에 is_valid에서 저필드를 검사 진행해 버려.
    # 그래서 read_only = True해주는 것.
    comments = CommentSerializer(many=True, read_only = True)
    
    # 예전 orm중에
    # article.comment_set.count() 이런 orm있었음 .count()는 쿼리셋 api
    # 위 명령어를 안쪽에 쓸 수 있고 위 시리얼라이저는 아티클 모델로 만들어져.
    # 그래서 article은 제외하고 그 뒤쪽의 값들만 comments.count라고 입력해줘.
    # 나는 강의랑 다르게 related_name을 comments로 지정해줘서 comments로 해준 것.
    comment_count = serializers.IntegerField(source='comments.count', read_only=True)
    # source는 필드를 채우는 데 사용할 속성의 이름.
    # 점 표기법(dotted notation)을 사용하여 속성을 탐색함.
    class Meta:
        model = Article
        fields = '__all__'

# 댓글은 단일 조회, 전체 조회 모두 하나의 시리얼라이저 사용
class CommentSerializer(serializers.ModelSerializer):
    # 클래스 메타의 역할 궁금해서 검색
    # DB Table에 이름을 지정해주는 등 모델의 정보를 정해주는 역할
    # 어떤 모델을 사용할지 정의하며, 해당모델에서 어떤 필드 사용할지 정의

    # 기본 출력이 아니라 override진행할 것. 새로운 값으로 출력할 수 있도록,title출력 할 수 있또록
    # title필드만 변환해주는 변환기 (시리얼라이저)필요
    class ArticleSerializer(serializers.ModelSerializer):
        class Meta:
            model = Article
            fields = ('id','title',)
    # override하는 순간, 59번 코드 read_only_fields비활성화됨.
    # 그래서 아티클 시리얼 라이저 인자에 read_only=True
    article = ArticleSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = '__all__'
        # 이렇게 해주면 유효성검사에서는 제외되고 조회할때는 사용된다는 의미.
        # read_only_fields = ('article',)



# 주의 
# 특정필드를 override 혹은 추가한 경우 read_only_fields는 동작하지 않음
# 해당필드의 read_only인자로 작성해야 함.