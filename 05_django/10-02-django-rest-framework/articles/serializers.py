from rest_framework import serializers
from .models import Article, Comment

class CommentSerializer(serializers.ModelSerializer):
    #override title만 출력할 수 있도록
    class ArticleSerializer(serializers.ModelSerializer):
        class Meta:
            model = Article
            fields = ('title',)
    
    # override
    article = ArticleSerializer(read_only=True)
    
    
    class Meta:
        model = Comment
        fields ='__all__'
        # read_only_fields = ('article',)\
        # read_only_fields란 하나의 변수라기 보다는  read_only_fields = ('필드명',)이 하나의 기능을 나타내는 명령어라고 생각.
        # 튜플이라는 걸 알기 위해 안에 요소 하나일때도 ',' 찍어줌.

class ArticleListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('id', 'title', 'content',)


class ArticleSerializer(serializers.ModelSerializer):
    comment_set = CommentSerializer(many=True, read_only=True)
    # article.comment_set.count()
    comment_count = serializers.IntegerField(source='comment_set.count', read_only=True)
    # 그 시리얼 라이저 클래스가 어떤 정보들로 이루어질 것인가를 정의하는 곳. == Meta
    class Meta:
        model = Article
        fields = '__all__'

# serializer는 아래 정의된 model의 fields로 정의된 데이터를 읽을 수 있도록 해주는 것.
# class syrializer 어쩌구로 한번 class가 정의되고 아래에서 class명이 나오면 그 class의 기능이 정의 되는 것.