from django import forms
from .models import Book


# form 태그와 관련된 기능을 하는
# 어떠한 클래스를 만들건데...
# 그 form태그 구성물들을 models에 정의한
# 어떤 class의 정보를 토대로 만들거야.
class BookForm(forms.ModelForm):

    class Meta:
        model = Book
        # fields = '__all__'
        # fields = ('title', 'description', 'adult', 'price')
        exclude = ('author', )
