from rest_framework import serializers
from .models import Article,Comment

class CommentSerializer(serializers.ModelSerializer):
    #override title만 출력할 수 있도록
    class ArticleSerializer(serializers.ModelSerializer):
        class Meta:
            model = Article
            fields = ('title',)
    
    # override
    article = ArticleSerializer()
    
    
    class Meta:
        model = Comment
        fields ='__all__'
        # read_only_fields = ('article',)
        # 튜플이라는 걸 알기 위해 안에 요소 하나일때도 ',' 찍어줌.

class ArticleListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('id', 'title', 'content',)


class ArticleSerializer(serializers.ModelSerializer):
    comment_set = CommentSerializer(many=True, read_only=True)
    # article.comment_set.count()
    comment_count = serializers.IntegerField(source='comment_set.count', read_only=True)
    
    class Meta:
        model = Article
        fields = '__all__'

