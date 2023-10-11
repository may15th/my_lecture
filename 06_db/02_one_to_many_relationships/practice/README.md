# 도서 관리 서비스 만들기

- 도서와 저자 정보를 1:N 관계로 관리 할 수 있는 프로젝트를 진행하고자 한다. 요구 사항을 만족하는 코드를 작성하시오.

### 요구 사항

- gitignore를 포함하여야 한다.
- 새로운 가상 환경을 생성하고, 가상 환경 내에서 django를 설치한다.
- project 명은 libraries_management로 생성한다.
- app 명은 libraries로 생성한다.
- Author model과 Book Model을 정의한다.
    - 정의해야 할 필드 정보는 첨부 파일을 참고
    - 저자와 도서는 1:N 관계를 맺는다.
    
- 관리자 페이지에서 두 모델을 모두 관리 할 수 있어야 한다.
    - 관리자 페이지에서 저자 목록 정보에서 각 저자의 이름이 표기되도록 model에 매직메서드를 활용하여 설정한다.
    - 관리자 페이지에서 저자를 최소 2개 이상 생성한다.

- 저자 전체 목록을 확인 할 수 있는 페이지를 제공한다.
- 저자 상세 정보를 확인 할 수 있는 페이지를 제공한다.

- 저자 상세 정보 페이지에서 책 정보를 생성 할 수 있는 기능을 구현한다.
    - '/libraries/{author_pk}/books/create/' 경로로 요청을 보낸다.
    - ModelForm을 사용하여 form을 구성한다.
    - 책 정보 생성시 저자 객체는 사용자가 직접 선택하지 않도록 form을 구성한다.
    - 책 정보 생성이 완료되면 저자 상세 정보 페이지로 redirect한다.
- 저자 상세 정보 페이지에서 저자를 참조하고 있는 책의 제목을 모두 보여준다.
- 저자 전체 목록에서는 각 저자를 참조하고 있는 책의 수를 보여준다.


### 느낀점
createsuperuser 한 이후에
관리자 페이지에서 이상하게 로그인이 안됐었는데,
아마 app-admin.py에서 아래처럼 등록을 안했기 때문이었던 것 같다. 기억하자...

from django.contrib import admin
from .models import Author, Book

# Register your models here.
admin.site.register(Author)
admin.site.register(Book)

model파일의 Author, Book 클래스를 임포트 해주고
admin.site.register에 각각 등록해준다.!!


pjt url.py에도 