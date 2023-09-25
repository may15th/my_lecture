from django.urls import path
from . import views

app_name = 'articles'
urlpatterns = [
    path('index/', views.index, name ='index')
]

#articles views.py에서 받아올 것.
# oop처럼 객체처럼 처리할 거니깐 이름으로 다루겠다.