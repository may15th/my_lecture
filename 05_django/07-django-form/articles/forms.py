from django import forms
from .models import Article

# class ArticleForm(forms.Form):
#     title = forms.CharField(max_length=10)
#     content = forms.CharField(widget=forms.Textarea)


class Article(forms.ModelForm):
    # model 등록만 하면 돼
    class Meta: 
        model = Article
        fields = '__all__'
        # fields = ('title', )
        # exclude = ('title',)
    
