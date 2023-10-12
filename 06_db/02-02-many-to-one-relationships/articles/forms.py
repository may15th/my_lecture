from django import forms
from .models import Article, Comment

# NOT NULL constraint failed: articles_article.user_id 

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        # fields = ('title', 'content')
        exclude = ('user',)

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)
