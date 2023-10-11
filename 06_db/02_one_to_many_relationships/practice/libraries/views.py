from django.shortcuts import render, get_object_or_404
from .models import Author

def authors(request):
    # 어떻게 db에서 특정 recode들 가져올 수 있는가.
    # objects가 가지고있는 all() query ser api사용하면 된다.
    # 이부분 다시 인강 보기.
    # 함수 호출 결과를 변수에 담는다.
    authors = Author.objects.all()  # model
    context = {
        'authors' : authors,
    }
    return render(request, 'libraries/authors.html', context)

def detail(request, author_pk):
    author = Author.objects.get(pk=author_pk)
    context = {
        'author' : author
    }
    return render(request, 'librares/detail.html', context)