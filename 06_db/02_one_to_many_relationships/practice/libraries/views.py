from django.shortcuts import render, redirect
from .models import Author, Book
from .forms import BookForm

# Create your views here.
# View 함수가 할일
def authors(request):
    # data base에서 특정 record를 가져 올 수 있는가?
    # sql -> SELECT * FROM libraries_authors;

    # 전체 저자 목록을 보여주기
    # 함수 호출 결과를 변수에 담는다.
    authors = Author.objects.all()
    # 전체 저자 목록 -> Model
    # model에서 받아와서 사용자한테는 어떻게 보여 줄건데?
    # Template
    context = {
        'authors': authors
    }
    return render(request, 'libraries/authors.html', context)

def detail(request, author_pk):
    # html을 꾸밀 내용 -> pk값이 사용자가 주소창에 입력한
    # author_pk와 일치하는 데이터의 정보로 화면을 구성하겠다.
    # SELECT * FROM libraries_authors WHERE pk = author_pk;
    author = Author.objects.get(pk=author_pk)
    # 나를 참조 하고 있는 객체들만 다뤄주는 매니저
    # 역참조 매니저
    # 나를 참조 하고있는 class명 _ set 이라는 이름으로 매니저명이 만들어진다.
    # 1에 대해서 N개의 책들
    books = author.book_set.all()
    book_count = author.book_set.count()
    print(book_count)

    book_form = BookForm()
    # print(Book.objects.filter(author_id=author_pk))
    context = {
        'author': author,
        'book_form': book_form,
        'books': books
    }
    return render(request, 'libraries/detail.html', context)


def book_create(request, author_pk):
    author = Author.objects.get(pk=author_pk)
    form = BookForm(request.POST)
    if form.is_valid():
        '''
        INSERT INTO libraries_books 
            (title, description, adult, price)
        VALUES
            (제목, 설명, False, 123);
        '''
        # book 객체에 추가해야 될 데이터가 있으니,
        # 잠시 db에 직접 commit을 남기지는 말고 instance 만 생성해봐
        book = form.save(commit=False)
        book.author = author
        book.save()
        # detail페이지는 필요로한다. -> author pk
    return redirect('libraries:detail', author_pk)