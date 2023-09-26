from django import forms
from .models import Article

# class ArticleForm(forms.Form):  # forms라는 모듈 안에 Form이라는 클래가 존재 한다. models라는 모듈 안에 Form이라는 클래스 존재 한 것과 같다.
#     title = forms.CharField(max_length=10)  # 모델필드와 거의 동일하다
#     content = forms.CharField(widget=forms.Textarea) # 문자열 필드는  charfiels로! models와 차이점.
#     # 정해진 빌트인 위젯이 있어서 form형태를 바꿔주는 것.

class Article(forms.ModelForm):
    # model 등록만 하면 돼
    class Meta: 
        model = Article
        # fields = '__all__'
        fields = ('title', )
        exclude = ('title',)
    
