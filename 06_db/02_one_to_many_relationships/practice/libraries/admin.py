from django.contrib import admin
from .models import Author, Book

# Register your models here.
# Author, Book 클래스를 등록한다.
admin.site.register(Author)
admin.site.register(Book)

# admin 에서 사이트 등록을 안해서 접속 안됐던 것 같다...